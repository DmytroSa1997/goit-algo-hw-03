from datetime import datetime

def get_days_from_today(date_str):
    """
    Обчислює кількість днів від заданої дати до поточної.
    Якщо задана дата пізніша за поточну, повертає від'ємне число.

    Параметри:
        date_str (str): Рядок дати у форматі 'РРРР-ММ-ДД'.

    Повертає:
        int: Різниця у днях між поточною датою і заданою.
        str: Повідомлення про помилку, якщо формат дати некоректний.
    """
    try:
        # Перетворення рядка у об'єкт date.
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        # Повертаємо повідомлення про помилку, якщо формат дати некоректний.
        return "Невірний формат дати. Використовуйте 'РРРР-ММ-ДД'."

    # Отримання поточної дати.
    today = datetime.today().date()

    # Розрахунок різниці днів.
    delta = today - given_date
    return delta.days


# Приклад використання:
if __name__ == "__main__":
    # Тест з коректними даними
    result = get_days_from_today("2021-10-09")
    print(result)  # Виведе кількість днів (наприклад, 157)

    # Тест з некоректними даними
    result = get_days_from_today("2021/10/09")
    print(result)  # Виведе: Невірний формат дати. Використовуйте 'РРРР-ММ-ДД'.

import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує список унікальних випадкових чисел у заданому діапазоні.

    Параметри:
        min (int): Мінімальне можливе число у наборі (не менше 1).
        max (int): Максимальне можливе число у наборі (не більше 1000).
        quantity (int): Кількість чисел, які потрібно вибрати (значення між min і max).

    Повертає:
        list: Відсортований список унікальних випадкових чисел.
              Якщо параметри не відповідають обмеженням, повертає пустий список.
    """
    # Перевіряємо коректність вхідних параметрів
    if not (1 <= min <= max <= 1000) or not (1 <= quantity <= (max - min + 1)):
        return []  # Повертаємо пустий список, якщо параметри недійсні

    # Використовуємо множину для забезпечення унікальності чисел
    unique_numbers = set()

    # Генеруємо унікальні числа, поки не отримаємо потрібну кількість
    while len(unique_numbers) < quantity:
        number = random.randint(min, max)  # Генеруємо випадкове число у діапазоні
        unique_numbers.add(number)  # Додаємо число до множини

    # Перетворюємо множину у відсортований список
    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers


# Приклад використання функції
if __name__ == "__main__":
    # Тест з коректними даними
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)  # Наприклад: [4, 15, 23, 28, 37, 45]

    # Тест з некоректними даними
    invalid_numbers = get_numbers_ticket(10, 5, 3)
    print("Спроба з некоректними даними:", invalid_numbers)  # Виведе: []

import re


def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    # Перевіряємо, чи номер починається з '+' або '380'
    if cleaned_number.startswith("+"):
        # Якщо номер вже містить міжнародний код, повертаємо його
        return cleaned_number
    elif cleaned_number.startswith("380"):
        # Якщо номер починається з '380', додаємо '+' на початку
        return f"+{cleaned_number}"
    else:
        # Якщо номер не містить міжнародного коду, додаємо '+38'
        return f"+38{cleaned_number}"


# Приклад використання функції
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)