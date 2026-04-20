import json
import logging
import os
import sys
from time import strftime

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    encoding="utf-8"
)
TASKS_FILE = "tasks.json"
LOG_FILE = "app.log"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

def parse_cli() -> None:
    """Парсит аргументы командной строки и запускает соответствующую команду."""

    if len(sys.argv) < 2:
        print("Использование: python task_manager.py <команда> [аргументы]")
        logging.warning("Запущен без аргументов")
        return
    command = sys.argv[1]
    arguments = sys.argv[2:]
    logging.info(f"Вызов команды: {command}")

    if command == "add":
        task_text = " ".join(arguments)
        if not task_text:
            print("Использование: python task_manager.py <команда> [аргументы]")
            logging.warning("Запущен без аргументов")
            return
        logging.info(f"Подготовка к добавлению задачи: {task_text}")
        tasks = load_tasks(TASKS_FILE)
        new_id = max((t["id"] for t in tasks), default=0)+1
        new_task = {
            "id": new_id,
            "text": task_text,
            "created_at": strftime("%Y/%m/%d %H:%M:%S"),
            "done": False,
        }
        tasks.append(new_task)
        save_tasks(tasks, TASKS_FILE)
        logging.info(f"Задача #{new_id} добавлена")
        print(f"Задача #{new_id} добавлена")
    elif command == "list":
        logging.info("Запрос списка задач")
        tasks = load_tasks(TASKS_FILE)

        if not tasks:
            print("список задач")
            return
        print(f"\n📋 Задачи ({len(tasks)}):")
        print("-" * 40)
        for t in tasks:
            status = "✓" if t.get("done" , False) else  "X"
            created = t.get("created_at", "?")
            print(f"{t['id']}. [{status}] {t['text']}")
            print(f"   🕐 {created}")
        print("-" * 40)
    elif command == "delete":
        if not arguments:
            print("Ошибка: укажи номер задачи")
            logging.warning("Команда delete без номера")
            return
        task_id = arguments[0]
        try:
            task_id = int(task_id)
        except ValueError:
            print(f"Ошибка: '{task_id}' не является числом")
            logging.warning(f"delete получен невалидный id:{task_id}")
            return
        logging.info(f"Подготовка к удалению задачи №{task_id}")
        tasks = load_tasks(TASKS_FILE)
        original_len = len(tasks)
        tasks = [t for t in tasks if t["id"] != task_id]


        if len(tasks) == original_len:
            print(f"❌ задача не найдена: {task_id}")
            logging.warning(f"задача не найдена: {task_id}")

        else:
            logging.info("Задача #%s успешно удалена", task_id)
            logging.info(f"Задача #{task_id} удалена")
            print(f"✓ Задача #{task_id} удалена")
            return




def load_tasks(path: str) -> list[dict]:
    """Загружает список задач из JSON-файла. Возвращает пустой список при ошибке."""

    if not os.path.isfile(path):
        logging.info(f"Ошибка: файл {path} не найден")
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except json.decoder.JSONDecodeError:
        logging.error("Файл повреждён: невалидный JSON")
        return []
    except PermissionError:
        logging.error("Нет прав на чтение файла")
        return []
    except Exception as e:
        logging.error(f"Неожиданная ошибка: {e}")
        return []
def save_tasks(tasks: list[dict], path: str) -> None:
    """Сохраняет список задач в JSON-файл. Логирует ошибки записи."""

    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
            logging.info("Задачи сохранены")
    except TypeError:
        logging.error("Ошибка: данные не нереализуемы")
    except IOError:
        logging.error("Ошибка записи файла")
    except OSError:
        logging.error("Ошибка записи файла")
    except Exception as e:
        logging.error(f"Неожиданная ошибка: {e}")



if __name__ == "__main__":
    parse_cli()
