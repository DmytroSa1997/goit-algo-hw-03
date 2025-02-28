def total_salary(path):
    """
    Функція total_salary аналізує текстовий файл, де кожен рядок містить дані про зарплату розробника.
    Дані мають формат: "Ім'я Прізвище,зарплата" (без пробілів після коми).

    :param path: шлях до текстового файлу з даними.
    :return: кортеж (total, average) або None у випадку помилки.
    """
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # Видаляємо пробільні символи на початку та в кінці
                if not line:
                    continue  # Пропускаємо порожні рядки
                parts = line.split(',')
                if len(parts) != 2:
                    print(f"Невірний формат рядка: {line}")
                    continue
                try:
                    salary = float(parts[1])
                except ValueError:
                    print(f"Не вдалося перетворити зарплату '{parts[1]}' у число.")
                    continue
                total += salary
                count += 1
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено!")
        return None
    except Exception as e:
        print(f"Виникла помилка при обробці файлу: {e}")
        return None

    if count == 0:
        return (0, 0)
    average = total / count
    return (total, average)
if __name__ == "__main__":
    file_path = r"C:\Users\ДмитроСавоста\OneDrive - Ukrfinzhytlo\Робочий стіл\Новий Текстовий документ.txt"
    result = total_salary(file_path)
    if result is not None:
        total, average = result
        print(f"Загальна сума заробітної плати: {total}")
        print(f"Середня заробітна плата: {average}")


def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:  # Переконуємось, що є три значення
                    cat_id, name, age = parts
                    cats_info.append({"id": cat_id, "name": name, "age": age})
        return cats_info
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return []

# Виклик функції
file_path = r"C:\Users\ДмитроСавоста\OneDrive - Ukrfinzhytlo\Робочий стіл\Новий Текстовий документ (2).txt"
cats_info = get_cats_info(file_path)

print(cats_info)




def parse_input(user_input):
    """Розбиває введений рядок на команду та аргументи."""
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    return command, args

def add_contact(args, contacts):
    """Додає новий контакт до словника."""
    if len(args) != 2:
        return "Invalid command. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    if len(args) != 2:
        return "Invalid command. Usage: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return f"Contact '{name}' not found."

def show_phone(args, contacts):
    """Показує номер телефону для зазначеного контакту."""
    if len(args) != 1:
        return "Invalid command. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact '{name}' not found."

def show_all(contacts):
    """Показує всі збережені контакти."""
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    """Основна функція, яка керує циклом запит-відповідь."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()