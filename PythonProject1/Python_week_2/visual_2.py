import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    """
    Используй sales.csv (или создай новый дата сет с датами,
    если хочешь линейный график).
Напиши visualizer.py, который:
Загружает данные в DataFrame
Строит 2 графика:
Столбчатая диаграмма (bar): общие продажи по менеджерам
Круговая (pie) или столбчатая: доля продаж по регионам
Добавляет к каждому: заголовок, подписи осей, значения на графиках (если применимо), легенду
Сохраняет оба графика в .png с dpi=150
Оборачивает логику в main() -> None с docstring
    :return:
    """
    df = pd.read_csv('sales_raw.csv', encoding='utf-8')
    """Процесс очистки и подготовки данных для построение графика"""
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
    """

    mgr_sale = df.groupby('manager')['amount'].sum()
    print(mgr_sale)
    mgr_sale.plot(kind='bar' , title="Продажа по менеджерам ", figsize=(6,4))
    plt.xlabel("Менеджер")
    plt.ylabel("Сумма продаж , руб")  # Подписывает ось Y (левую).
    plt.tight_layout()
    plt.show()
    plt.savefig("manager.png", dpi=150, bbox_inches="tight")

    region_sale = df.groupby('region')['amount'].sum()
    region_sale.plot(kind='pie', title = '123',figsize=(6,4))
    plt.xlabel("Менеджер")
    plt.ylabel("Сумма по региону , руб")  # Подписывает ось Y (левую).
    plt.tight_layout()
    plt.show()"""
    print("выберите тип графика \n"
          "столбцовый = 1\n"
          "круговой = 2\n")
    user_input = int(input("введите одно из чисел: "))
    try:
        if user_input == 1:
            mgr_sale = df.groupby('manager')['amount'].sum()
            print(mgr_sale)
            mgr_sale.plot(kind='bar', title="Продажа по менеджерам ", figsize=(6, 4))
            plt.xlabel("Менеджер")
            plt.ylabel("Сумма продаж , руб")  # Подписывает ось Y (левую).
            plt.tight_layout()
            plt.show()
            plt.savefig("manager.png", dpi=150, bbox_inches="tight")

        elif user_input == 2:
            region_sale = df.groupby('region')['amount'].sum()
            print(region_sale)
            region_sale.plot(kind='pie', title='Регионы', figsize=(6, 4))
            plt.xlabel("Менеджер")
            plt.ylabel("Сумма по региону , руб")  # Подписывает ось Y (левую).
            plt.tight_layout()
            plt.show()
            plt.savefig("region.png", dpi=150, bbox_inches="tight")
    except TypeError:
        print('error')
        return


if __name__ == '__main__':
    main()

