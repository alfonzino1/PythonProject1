"""
Напиши функцию get_even_lengths(text: str) -> list[int], которая:
Разбивает входную строку на слова.
Считает длину каждого слова.
Оставляет только те длины, которые делятся на 2 без остатка.
Возвращает список этих длин.
❌ не работает
📍 Строка 3: len(text) после split() возвращает количество слов, а не длину каждого слова.
📍 Строка 3: if len(text) % 2 == 0: проверяет, чётно ли число слов в списке, а не длины отдельных слов.
📍 Строка 4: map(int, text) пытается преобразовать слова (например, "hello") в числа. При запуске это вызовет ValueError.
🔄 Что нужно исправить:
Пройтись циклом по каждому слову из списка.
Для каждого слова взять его длину (len(слово)).
Проверить, делится ли эта длина на 2.
Собрать подходящие длины в новый список и вернуть его.
"""
"""
import string

from testing import text


def get_even_length(text: str) -> list[int]:
    result = []
    for word in text.split():
        if len(word) % 2 == 0:
            result.append(len(word))
    return result
"""
"""
функция get_even_length(с параметрами text: srt строка) аннотацию типу List[int]
создаётся пустой словарь result = []
создаёется цикл for в нём переменная word перебирает переменную text у который вызван split() который делит слова на 
отдельные буквы и приобразует их в Int
в дальнейшем условия If с методом len проверяет равна ли переменная word условию деленния без остатка на 2
if len(word) % 2 == 0:
и то что подходит под условия пишет в словарь result
и в конце функция через метод retunr выводит результат глобально
"""
"""
Ты отлично стараешься формулировать логику вслух — это важный шаг для закрепления. Но в описании есть 4 технических неточности, которые нужно чётко разделить, иначе дальше будет путаница в терминах и типах данных.
🔍 Разбор по пунктам:
1️⃣ result = [] → это список (list), а не словарь. Словарь в Python создаётся фигурными скобками {}. Твоя аннотация -> list[int] верна, поэтому [] здесь правильный выбор.
2️⃣ split() не разбивает на буквы и не преобразует в int. Он разрезает строку на слова по пробелам/переносам. Результат: список строк ["hello", "world", "python"]. Никакого приведения к числам здесь нет.
3️⃣ В result.append(...) ты добавляешь не слово, а его длину (len(word)). Метод len() сам возвращает целое число, поэтому int() не нужен.
4️⃣ return не делает переменную глобальной. Он просто передаёт готовый список обратно в то место, откуда вызвали функцию (например, в main()). Глобальные переменные — это отдельный механизм, и в твоём коде они не используются.
💡 Как звучит технически точно:
"Функция принимает строку. Делит её на слова. Для каждого слова вычисляет длину. Если длина делится на 2 без остатка → это число добавляется в пустой список. В конце список возвращается вызывающему коду."
Теперь картина чистая. Ты понимаешь разницу между данными и операциями над ними
"""
"""
Напиши функцию find_duplicates(numbers: list[int]) -> dict[int, int], которая:
Принимает список целых чисел.
Считает, сколько раз каждое число встречается в списке.
Возвращает словарь только с теми числами, которые встречаются строго больше 1 раза.
Если дубликатов нет → возвращает пустой словарь {}.
📍 Строка 4: if number in duplicates: → условие всегда ложно, потому что ты никогда не добавляешь ключ в словарь при первом появлении числа. Словарь остаётся пустым {} на всём протяжении цикла.
📍 Требование ТЗ: Функция должна вернуть только те числа, которые встречаются > 1 раза. Даже если подсчёт заработает, сейчас в результат попадут все числа, включая те, что встретились единожды.
🔄 Что исправить (структурно):
В цикле добавь логику для первого вхождения: если числа ещё нет в словаре → запиши его со значением 1. Если уже есть → увеличь счётчик на 1.
После завершения цикла создай новый словарь (или отфильтруй текущий), оставив только пары, где значение (частота) строго больше 1.
Верни отфильтрованный словарь через return
"""
""""
def find_duplicates(numbers: list[int]) -> dict[int, int]:
    duplicates = {}
    for number in numbers:
        if number not in duplicates:
            duplicates[number] = 1
        else:
            duplicates[number] += 1
    duplicate = {}
    for num, count in duplicates.items():
        if duplicates > 1:
            duplicate.append(duplicate)
    return duplicate
"""
"""
stroka = " Python , is awesome! "
text = stroka.strip()
text = text.split(",")
clean = []
for test in text:
    test = test.strip()
    clean.append(test)
clean ="-".join(clean)
clean = clean.split("-")
clean = clean[::-1]
print(clean)


sps = [1, 2, 2, 3, 4, 4, 4, 5]
unique = []
for a in sps:
    if a not in unique:
        unique.append(a)
spisok = [x * 2 for x in unique]
print(spisok)

"""
"""
def safe_divide(a: str, b: str) -> float | None:
    try:
        return float(a) / float(b)
    except ZeroDivisionError:
        print("[LOG] Ошибка: деление на ноль")
        return None
    except ValueError:
        print('[LOG] Ошибка: передано не число')
        return None
    finally:
        print("[LOG] Операция завершена")
safe_divide("10", "2")
safe_divide("10", "0")
safe_divide("abc", "2")
safe_divide("5", "3")

"""

"""
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Привет, мир!")
# файл закрылся сам, даже если бы код ниже вызвал ошибку
образец
with open('text.txt',"w" ,encoding="utf-8") as file:
    file.write("data")
with open('text.txt',"r" ,encoding="utf-8") as file:
    print(len(file.read()))
"""
"""
def write_and_read(data: str, path: str) -> int:
    with open(path,"w", encoding="utf-8") as file:
        file.write(data)
    with open(path,"r",encoding="utf-8") as file:
        return len(file.read())

"""



"""
import string
import json
from _datetime import datetime
def save_dict_to_json(data: dict, path: str) -> bool:
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

            return True
    except TypeError:
        print("[LOG] Ошибка: данные не нереализуемы")
        return False
def read_input(path: str) -> str | None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("[LOG] Ошибка: файл не найден")
        return None
    except PermissionError:
        print("[LOG] Ошибка: нет прав на чтение")
        return None
    except Exception as e:
        print(f"[LOG] Ошибка: {e}")
        return None
def count_words(text: str) -> dict[str, int]:
    text = text.lower()
    for tochka in string.punctuation:
        text = text.replace(tochka, '')

    words = text.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    report = []
    report["processed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def main() -> None:
    print("[LOG] Старт анализа текста")
    text = read_input("input.txt")
    if text is None:
        print("[LOG] Чтение отменено")
        return
    print("[LOG] Чтение завершено. Начинаю обработку")
    counts = count_words(text)
    print("[LOG] Подсчёт завершён. Сохраняю результат")

    success = save_dict_to_json(counts, "output.json")
    if success:
        print("[LOG] Готово! Результат в output.json")
    else:
        print("[LOG] Ошибка сохранения")
if __name__ == "__main__":
    main()
"""

import string
import json
from datetime import datetime
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    encoding="utf-8"
)

def read_input(path: str) -> str | None:
    """Безопасно читает текст из файла."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logging.error("[LOG] Ошибка: файл не найден")
        return None
    except PermissionError:
        logging.error("[LOG] Ошибка: нет прав на чтение")
        return None
    except Exception as e:
        logging.error(f"[LOG] Ошибка: {e}")
        return None


def count_words(text: str) -> dict[str, int]:
    """Считает частоту слов без учёта регистра и знаков препинания."""
    text = text.lower()
    for punct in string.punctuation:
        text = text.replace(punct, '')

    words = text.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def save_dict_to_json(data: dict, path: str) -> bool:
    """Сохраняет словарь в JSON с обработкой ошибок сериализации."""
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
            return True
    except TypeError:
        logging.error("[LOG] Ошибка: данные не сериализуемы")
        return False


def main() -> None:
    """Точка входа. Собирает пайплайн: чтение → подсчёт → отчёт → сохранение."""
    logging.info("[LOG] Старт анализа текста")

    text = read_input("input.txt")
    if text is None:
        logging.error("[LOG] Чтение отменено")
        return

    logging.info("[LOG] Чтение завершено. Начинаю обработку")
    counts = count_words(text)

    logging.info("[LOG] Подсчёт завершён. Сохраняю результат")

    # Сборка финального отчёта по ТЗ
    sorted_pairs = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    top_3 = [{"word": w, "count": c} for w, c in sorted_pairs[:3]]

    report = {
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_words": sum(counts.values()),
        "top_3": top_3
    }

    success = save_dict_to_json(report, "output.json")
    if success:
        logging.info("[LOG] Готово! Результат в output.json")
    else:
        logging.error("[LOG] Ошибка сохранения")


if __name__ == "__main__":
    main()

