import os

DATA_FILE = "phonebook.txt"


def add_entry() -> None:
    """
    Добавляет новую запись в телефонный справочник.

    Запрашивает пользователя ввести информацию о новой записи и сохраняет её в файл.
    """
    with open(DATA_FILE, "a") as f:
        f.write(
            input("Введите фамилию: ") + ","
            + input("Введите имя: ") + ","
            + input("Введите отчество: ") + ","
            + input("Введите название организации: ") + ","
            + input("Введите рабочий телефон: ") + ","
            + input("Введите личный телефон: ") + "\n"
        )
    print("Запись успешно добавлена!")


def edit_entry() -> None:
    """
    Редактирует существующую запись в телефонном справочнике.

    Позволяет пользователю изменить информацию в записи по заданной фамилии.
    """
    search_term = input("Введите фамилию для поиска записи: ")
    temp_file = "temp.txt"

    with open(DATA_FILE, "r") as f, open(temp_file, "w") as temp:
        for line in f:
            if search_term in line:
                print("Редактирование записи:")
                new_line = (
                        input("Введите фамилию: ") + ","
                        + input("Введите имя: ") + ","
                        + input("Введите отчество: ") + ","
                        + input("Введите название организации: ") + ","
                        + input("Введите рабочий телефон: ") + ","
                        + input("Введите личный телефон: ") + "\n"
                )
                temp.write(new_line)
            else:
                temp.write(line)

    os.remove(DATA_FILE)
    os.rename(temp_file, DATA_FILE)
    print("Запись успешно отредактирована!")


def display_entries(page_size: int = 10) -> None:
    """
    Выводит записи из телефонного справочника постранично.

    :param page_size: Количество записей на странице.
    """
    with open(DATA_FILE, "r") as f:
        entries = f.readlines()
        total_entries = len(entries)
        num_pages = (total_entries // page_size) + 1

        for page in range(num_pages):
            print("\nСтраница", page + 1, "из", num_pages)
            start_idx = page * page_size
            end_idx = min((page + 1) * page_size, total_entries)
            for i in range(start_idx, end_idx):
                print(entries[i].strip())


def search_entries() -> None:
    """
    Выполняет поиск записей в телефонном справочнике по заданной строке.

    Запрашивает строку для поиска и выводит записи, в которых найдена эта строка.
    """
    search_term = input("Введите строку для поиска: ")
    with open(DATA_FILE, "r") as f:
        for line in f:
            if search_term in line:
                print(line.strip())


def main() -> None:
    """
    Основная функция для управления телефонным справочником.

    Отображает меню и позволяет пользователю выбирать опции.
    """
    while True:
        print("\nТелефонный справочник")
        print("1. Вывод записей постранично")
        print("2. Добавление новой записи")
        print("3. Редактирование записи")
        print("4. Поиск записей")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            display_entries()
        elif choice == "2":
            add_entry()
        elif choice == "3":
            edit_entry()
        elif choice == "4":
            search_entries()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий вариант.")


if __name__ == "__main__":
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w"):
            pass
    main()
