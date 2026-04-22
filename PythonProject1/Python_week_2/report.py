import pandas as pd
def main() -> None:
    """
    Загружает sales.csv
Заполняет пропуски (NaN) в region значением "Не указан", а в manager — "Система"
Строит сводную таблицу: manager (строки) × region (колонки), значения = сумма amount
Экспортирует результат в report_output.csv
Выводит в консоль краткую статистику (общая сумма, кол-во строк до/после очистки)
    :return:
    """

    df = pd.read_csv("sales.csv" , encoding="utf-8")
    rows_before = len(df)
    df = df.fillna({
        "manager":"Система",
        "region": "не указано"
    })
    rows_after = len(df)
    print(rows_before, "ДО ОЧИСТКИ")
    print(rows_after, "ПОСЛЕ")
    print("ОБЩАЯ СУММА ПРОДАЖ ",df["amount"].sum())
    pivot_df = df.pivot_table(
        index="manager",      # ← Строки: менеджеры
        columns="region",     # ← Столбцы: регионы
        values="amount",      # ← Что считаем: выручка
        aggfunc="sum",        # ← Как считаем: суммируем (не mean!)
        fill_value=0

    )
    print(pivot_df)
    pivot_df.to_csv(pivot_df = "output.csv" , index=True, header=True, encoding="utf-8")
if __name__ == "__main__":
    main()