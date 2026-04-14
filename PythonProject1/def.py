import random
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def guess_price_game() -> bool:
    target = random.randint(100, 10000)

    for attempt in range(1, 8):
        user_input = input(f"Попытка {attempt}/7. Введите цену: ")

        # 🛡 Блок обработки ошибок
        try:
            guess = int(user_input)
        except ValueError:
            print("⚠️ Пожалуйста, введите целое число (например, 5000)")
            continue  # ⏩ Пропускаем проверку, переходим к следующей попытке

        # 🎯 Основная логика игры (выполняется ТОЛЬКО если int() сработал)
        if guess == target:
            print("🎉 Поздравляю! Вы угадали цену.")
            logging.info(f"Пользователь угадал за {attempt} попыток")
            return True
        elif guess < target:
            print("📉 Слишком низко")
        else:
            print("📈 Слишком высоко")

    print(f"❌ Попытки кончились. Правильная цена была: {target}")
    logging.info(f"Пользователь проиграл. Правильный ответ: {target}")
    return False


def main():
    result = guess_price_game()
    print(f"Итог: {'Победа' if result else 'Поражение'}")


if __name__ == "__main__":
    main()