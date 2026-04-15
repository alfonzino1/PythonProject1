"""
ТЗ:
Сгенерируй список из 100 случайных цен от 100 до 15 000 руб. (random.randint).
Отфильтруй выбросы: убери всё, что < 500 или > 12 000.
Посчитай и выведи:
Среднее значение (sum / len)
Минимум и максимум
Количество товаров после фильтрации
Рефакторинг: сначала реши через циклы, потом перепиши расчёты в 1–2 строки с list comprehension.
Весь код — в функциях с аннотациями типов и docstring.
"""
import random
from typing import List
def generate_prices(count: int =100,min_val: int=100,max_val: int=15000)-> List[int]:
    """Генерирую список случайный цен"""
    return [random.randint(min_val, max_val) for _ in range(count)]
def filter_outlirers (prices: List[int],low: int = 500, high: int =12000) -> List[int]:
    """Фильтрует выбросы: оставляет только цены в диапазоне [low, high]"""
    return [p for p in prices if low <= p <= high]

def calculate_stats(prices: List[int]) -> dict:
    """Считает: count, mean, min, max. Обрабатывает пустой список."""
    if not prices:
        return {"count": 0, "mean": 0.0, "min": 0.0, "max": 0.0}

    count = len(prices)
    return {
        "count": float(count),
        "mean": round(sum(prices) / count),
        "min": float(min(prices)),
        "max": float(max(prices))}

def main() -> None:
    """Точка входа."""
    raw = generate_prices()
    filtered = filter_outlirers(raw)
    stats = calculate_stats(filtered)
    print(f"📊 Статистика: {stats}")

if __name__ == "__main__":
    main()