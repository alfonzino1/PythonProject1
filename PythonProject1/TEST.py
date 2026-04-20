def main() -> None:
    print("[LOG] Старт анализа текста")
    text = read_input("input.txt")
    if text is None:
        print("[LOG] Чтение отменено");
        return
    print("[LOG] Чтение завершено. Начинаю обработку")
    counts = count_words(text)
    print("[LOG] Подсчёт завершён. Сохраняю результат")
    success = save_dict_to_json(counts, "output.json")
    if success == True:
        print("[LOG] Чтение завершено. Начинаю обработку")
    else:
        print("[LOG] Подсчёт завершён. Сохраняю результат")