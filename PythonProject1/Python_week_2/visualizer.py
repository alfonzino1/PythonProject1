import matplotlib.pyplot as plt
import pandas as pd


def main()-> None:
    """Загружает данные, очищает их,
    строит столбчатую и круговую диаграммы, сохраняет в PNG."""
    df = pd.read_csv('sales_raw.csv', encoding='utf-8')
    # Процесс очистки и подготовки данных для построение графика
    # чистим столбцы от лишних символов
    df["amount"] = df["amount"].str.replace(r" руб\.| ", "", regex=True)
    # 2. Превращаем в числа (всё непонятное станет NaN
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    # во все пропуски в столбце amount поставить среднее значение по списку
    df["amount"] = df["amount"].fillna(df["amount"].median())
    # все пропуски в столбце регион поставить не указано
    df["region"] = df["region"].fillna("Не указан")
    # print(df)
    # переменная для рисования графика
    mgr_sale = df.groupby('manager')['amount'].sum()
    # print(mgr_sale)
    mgr_sale.plot(kind='bar' , title="Продажа по менеджерам ", figsize=(6,4))
    plt.xlabel("Менеджер")
    plt.ylabel("Сумма продаж , руб")  # Подписывает ось Y (левую).
    plt.tight_layout()
    plt.savefig("manager.png", dpi=150, bbox_inches="tight")
    plt.close()
    
    region_sale = df.groupby('region')['amount'].sum()
    region_sale.plot(kind='pie', title = "Доля продаж по регионам",figsize=(6,4))
    plt.tight_layout()
    plt.savefig("region.png", dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == '__main__':
    main()

