import pandas as pd
import json
import matplotlib.pyplot as plt
df = pd.read_csv("sales_march.csv" , encoding="utf-8")
# print(df.info())
# print(df.isna().sum())
# print(df.dtypes)
df["amount"] = df["amount"].str.replace(r" руб\.| ", "", regex=True)
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df["amount"] = df["amount"].fillna(df["amount"].median())
df["region"] = df["region"].fillna("Не указан")
mgr_sale = df.groupby('manager')['amount'].sum() # сумма по менеджерам
sgr_sale = df.groupby('region')['amount'].sum()  # сумма по регионам
tlt_sale = df['amount'].sum() # общая выручка
avg_sale = df['amount'].mean() # средний чек
#print("сумма продаж по менеджерам \n",mgr_sale)
#print("сумма продаж по регионам \n",sgr_sale)
#print("общая сумма продаж ",tlt_sale)
#print("средний чек \n",avg_sale)
mg_sale = mgr_sale.to_dict()
sg_sale = sgr_sale.to_dict()
report = {"by_manager": mg_sale,
          "by_region":sg_sale,
          "total_sum":tlt_sale,
          "avg_sum":avg_sale}
with open("report.json", "w",encoding="utf-8") as f:
   json.dump(report, f, ensure_ascii=False, indent=4)
mgr_sale.plot(kind="bar", title="продажи менеджеров",figsize = (6,4))
plt.xlabel("Менедежер")
plt.ylabel("Сумма продаж в руб")
plt.tight_layout()
plt.savefig("sales_manager.png", dpi=150, bbox_inches="tight")
plt.close()
sgr_sale.plot(kind="pie",title="Продажи по регионам",autopct="%.1f%%",figsize = (6,4))
plt.tight_layout()
plt.savefig("sales_region.png", dpi=150, bbox_inches="tight")
plt.close()
