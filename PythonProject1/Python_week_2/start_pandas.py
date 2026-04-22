import pandas as pd
def main() -> None:
    """Загружает CSV, фильтрует выбросы, выводит среднюю цену по категориям."""
    # 1. Загрузка
    # 2. Фильтрация
    # 3. Группировка + округление
    # 4. Вывод
    df = pd.read_csv("prices.csv", encoding="utf-8")
    filter_data = df[df["price"] < 10000]
    print(filter_data.groupby("category")["price"].mean().round(2))
if __name__ == "__main__":
    main()