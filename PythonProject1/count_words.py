# week1/day4/word_counter.py
import string
from typing import Dict, List, Tuple


# from collections import Counter  # для бонуса

def count_words(text: str) -> Dict[str, int]:
    # 1. Нормализация
    text = text.lower()

    # 2. Очистка (цикл работает только со строкой, слова ещё не трогаем)
    for tochka in string.punctuation:
        text = text.replace(tochka, '')

    # 3. Разбивка (вызываем ОДИН РАЗ, когда строка уже чистая)
    words = text.split()

    # 4. Подсчёт частот
    counts = {}
    for word in words:
        # .get() безопасно берёт текущее число или 0, если слова ещё нет
        """Считает частоту слов в тексте (без учёта регистра и знаков препинания)."""

        counts[word] = counts.get(word, 0) + 1

    # 5. Отдаём результат наружу
    return counts


def get_top_words(word_counts: Dict[str, int], top_n: int = 3) -> List[Tuple[str, int]]:
    """Возвращает топ-N самых частых слов."""
    # Твой код здесь
    sorted_pairs = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_pairs[:top_n]



def main() -> None:
    """Точка входа."""
    text = "Python is great. Python is powerful. I love Python!"
    counts = count_words(text)
    top = get_top_words(counts)

    emojis = ["🥇", "🥈", "🥉"]
    for i, (word, freq) in enumerate(top):
        print(f"{emojis[i]} {word}: {freq} раз")


if __name__ == "__main__":
    main()