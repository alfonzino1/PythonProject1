import string
from typing import Dict, List, Tuple
text = "Python is great. Python is powerful. I love Python!"
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
        counts[word] = counts.get(word, 0) + 1

    # 5. Отдаём результат наружу
    return counts

count_words(text)


