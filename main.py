# print("hello world \n")

# num = int(input("Enter an integer number: "))

# is_even = True if not num % 2 else False

# a = 0
# while a < 6:
#     a = a + 1
#     print("a % 2 =", a % 2)
#     if not a % 2:
#         continue
#     print(a)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0

# while num > 0:
#     sum += num
#     print(f"Num = {num}")
#     num -= 1
#     print(f"Sum = {sum}")

# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
# search = "r"
# result = 0
# for char in message:
#     if search == char:
#         result += 1
# print("result = ", result)  # 0 1 2 3 4
# print("Програма закінчена")

# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))
# gcd = first if first < second else second
# print ("gcdStart = ", gcd)
# while first % gcd or second % gcd:
#     gcd -= 1
#     print ("gcd = ", gcd)
# print ("gcdRes = ", gcd)


# message = input("Enter a message: ")
# offset = int(input("Enter the offset: "))
# encoded_message = ""
# for ch in message:
#     if 65 < ord(ch) < 90:
#         pos = ord(ch) - ord('A')  # 21
#         pos = (pos + offset) % 26  # 2
#         new_char = chr(pos + ord("A"))  # 'c'
#         print("new_char = ", new_char)
#         encoded_message += new_char
#     elif 97 < ord(ch) < 122:
#         pos = ord(ch) - ord('a')  # 21
#         pos = (pos + offset) % 26  # 2
#         new_char = chr(pos + ord("a"))  # 'c'
#         print("new_char2 = ", new_char)
#         encoded_message += new_char
#     else:
#         encoded_message += ch
#         print("ch", ch)
# print("encoded_message = ", encoded_message)

# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while True:
#     num = int(input("Enter integer (0 for output): "))
#     if num == 0:
#         break
#     for i in range(num + 1):
#         if i % 2:
#             continue
#         sum += i
#         print ("i = ", i, "sum = ", sum)
#     print("sum):", sum)

# result = 0
# operand = None
# operator = None
# wait_for_number = True
# wait_for_operator = True

# while True:
#     if wait_for_number:
#         try:
#             result = float(input("Enter number: "))
#             wait_for_number = False
#         except ValueError:
#             print("Please enter a number. Try again.")
#             continue
#     if wait_for_operator:
#         try:
#             operator = input("Enter operator + - * / (= for exit): ")
#             if operator == "=":
#                 print("result = ", result)
#                 break
#             if operator not in ("+", "-", "*", "/", "="):
#                 print("exept err operator: ", operator)
#                 continue
#             wait_for_operator = False
#         except ValueError:
#             print("Try enter an operator + - * / (= for exit): ")
#             continue
#     try:
#         operand = float(input("Enter number: "))
#         wait_for_operator = True
#     except ValueError:
#         print("Please enter a number. Try again.")
#         continue
#     if operator == "+":
#         result += operand
#     elif operator == "-":
#         result -= operand
#     elif operator == "*":
#         result *= operand
#     elif operator == "/":
#         if operand == 0:
#             print("Please enter not zero number: ")
#             wait_for_operator = False
#             continue
#         result /= operand
#     elif operator == "=":
#         print("result = ", result)
#         break

# a = ""
# def get_fullname(first_name, last_name="",  middle_name=""):
#     global a
#     if not middle_name and not last_name:
#         a = first_name
#     elif not middle_name:
#         a = first_name + " " + last_name
#     if not last_name:
#         a = first_name + " " + middle_name
#     else:
#         a = first_name + " " + middle_name + " " + last_name
#     print("Result:", a)
#     return a
# get_fullname(first_name="Petro", middle_name="Ivanovich")
# get_fullname(first_name="Petro", last_name="Zalizyak", middle_name="Ivanovich")
# get_fullname(first_name="Petro", last_name="Zalizyak")
# get_fullname(first_name="Petro")
# print(a)

# def format_string(string, length):
#     string_len = len(string)
#     if string_len < length:
#         space_len = (length - string_len) // 2
#         string = " " * space_len + string
#     print("string:", string)
#     return string
# format_string(string='aaagh', length=112)

# def first(size, *elements):
#     a = 0
#     a = len(elements) + size
#     print("first", a)
#     return a
# first(5, "sgfgf", "gdfg", "dfgdf")

# def factorial(n):
#     if n < 2:
#         return 1  # Базовий випадок
#     else:
#         return n * factorial(n - 1)
# def number_of_groups(n, k):
#     c_n_k = 0
#     c_n_k = factorial(n) // (factorial(n - k) * factorial(k))
#     return c_n_k
# print(number_of_groups(50, 7))

# def prepare_data(data):
#     if len(data) <= 1:
#         return data
#     data.sort()
#     data.pop(0)
#     data.pop(-1)
#     print(data)
#     return data
# data = [41, 3]
# prepare_data(data)

from functools import reduce
from collections import defaultdict
from datetime import datetime, timedelta
import collections
import shutil
import os
import base64
import re
import sys
from pathlib import Path
from random import randint

# ects_table = [
#     {
#         "Оцінка": 1,
#         "Бали": (0, 34),
#         "Оцінка ECTS": "F",
#         "Пояснення": "Unsatisfactorily",
#     },
#     {
#         "Оцінка": 2,
#         "Бали": (35, 59),
#         "Оцінка ECTS": "FX",
#         "Пояснення": "Unsatisfactorily",
#     },
#     {
#         "Оцінка": 3,
#         "Бали": (60, 66),
#         "Оцінка ECTS": "E",
#         "Пояснення": "Enough",
#     },
#     {
#         "Оцінка": 3,
#         "Бали": (67, 74),
#         "Оцінка ECTS": "D",
#         "Пояснення": "Satisfactorily",
#     },
#     {
#         "Оцінка": 4,
#         "Бали": (75, 89),
#         "Оцінка ECTS": "C",
#         "Пояснення": "Good",
#     },
#     {
#         "Оцінка": 5,
#         "Бали": (90, 95),
#         "Оцінка ECTS": "B",
#         "Пояснення": "Very good",
#     },
#     {
#         "Оцінка": 5,
#         "Бали": (96, 100),
#         "Оцінка ECTS": "A",
#         "Пояснення": "Perfectly",
#     },
# ]
# data = ects_table[:]
# for key in data:
#     # for k, value in key.items():
#     #     print(k, ':', value)
#     print(key)
# def get_grade(key):
#     global ects_table
#     for item in ects_table:
#         if item["Оцінка ECTS"] == key:
#             return item.get("Оцінка")
#     return None
# def get_description(key):
#     global ects_table
#     for item in ects_table:
#         if item["Оцінка ECTS"] == key:
#             return item.get("Пояснення")
#     return None
# # викликаю функції:
# key = "FX"
# grade = get_grade(key)
# description = get_description(key)
# if grade is not None:
#     print(f"Оцінка: {grade}")
# else:
#     print("Оцінка не знайдена")

# if description is not None:
#     print(f"Пояснення: {description}")
# else:
#     print("Пояснення не знайдено")
# data = {"Python": 1991, "Java": 1995, "JS": 1995}
# def lookup_key(data, value):
#     if value is None:
#         return []
#     result = []
#     for k, v in data.items():
#         print(k, ':', v)
#         if v == value:
#             result.append(k)
#     return result
# cent = lookup_key(data, None)
# print(cent)
# grade = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# grade = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# a = (5, 4, 3, 2, 1)
# x = sum(a)
# def split_list(grade):
#     if not isinstance(grade, (float, int, str, list, dict, tuple)):
#         return [], []
#     if not grade:
#         return [], []
#     average_grade = sum(grade) // len(grade)
#     sorted_grade = sorted(grade, reverse=False)
#     lower_or_equal = [
#         grade for grade in sorted_grade if grade <= average_grade]
#     greater = [grade for grade in sorted_grade if grade > average_grade]
#     print('lower_or_equal', lower_or_equal)
#     print('greater', greater)
#     return lower_or_equal, greater
# return tuple(lower_or_equal), tuple(greater)
# split_list(None)
# print(split_list([1, 12, 3, 24, 5]))
# def split_list(scores):
# Перевірка на порожній список
# if not scores:
#     return [], []
# Знаходимо середнє значення бала
# average_score = sum(scores) / len(scores)
# Розділяємо список на дві частини
# lower_or_equal = [score for score in scores if score <= average_score]
# greater = [score for score in scores if score > average_score]
# Повертаємо кортеж з двома списками
# return lower_or_equal, greater
# # Приклад використання:
# student_scores = [75, 82, 90, 65, 88, 72, 95, 60]
# lower_scores, greater_scores = split_list(student_scores)
# print("Значення менше або рівні середньому:", lower_scores)
# print("Значення більше середнього:", greater_scores)

# points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7,
#           (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
# def calculate_distance(coordinates):
#     if len(coordinates) <= 1:
#         return 0
#     global points
#     total_distance = 0
#     for i in range(len(coordinates) - 1):
#         point1, point2 = min(coordinates[i], coordinates[i + 1]), max(
#             coordinates[i], coordinates[i + 1])
#         print(f"min(coordinates[i={i}])", coordinates[i])
#         print(f"max(coordinates[i={i} + 1])", coordinates[i + 1])
#         print("point1", point1, "point2", point2)
#         distance = points[(point1, point2)]
#         total_distance += distance
#     return total_distance
# # Приклад використання:
# coordinates = [0, 1, 3, 2, 0]
# distance = calculate_distance(coordinates)
# print("Загальна відстань, яку пролетить дрон:", distance)

# def game(terra, power):
#     for sublist in terra:
#         print("sublist=", sublist)
#         for item in sublist:
#             if item <= power:
#                 power += item
#                 print("power=", power)
#             else:
#                 break
#     return power
# terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# initial_power = 1
# final_power = game(terra, initial_power)
# print("Загальна отримана енергія гравця:", final_power)

# def is_valid_pin_codes(pin_codes):
#     # Перевірка на порожній список
#     if not pin_codes:
#         return False
#     # Створюємо множину для зберігання унікальних пін-кодів
#     unique_pin_codes = set()
#     for pin_code in pin_codes:
#         if len(pin_code) != 4:
#             return False
#         # Перевірка, чи складається пін-код лише з цифр
#         if not pin_code.isdigit():
#             return False
#         # Додаємо пін-код до множини унікальних пін-кодів
#         unique_pin_codes.add(pin_code)

#     # Перевірка на наявність дублікатів
#     if len(unique_pin_codes) == len(pin_codes):
#         return True
#     else:
#         return False
# # Приклад використання:
# pin_codes = ['1101', '9034', '0011', '1101']
# result = is_valid_pin_codes(pin_codes)
# print("Чи є список валідним пін-кодом:", result)
# def get_random_password1():
#     # Створюємо пустий рядок для зберігання паролю
#     password = ""
#     # Генеруємо 8 символів для паролю
#     for _ in range(8):
#         # Генеруємо випадковий код символу в межах від 40 до 126 ASCII
#         random_num = randint(40, 126)
#         # Перетворюємо код символу у відповідний символ та додаємо його до паролю
#         password += chr(random_num)
#     return password

# def get_random_password():
#     password = ""
#     for i in range(8):
#         random_num = randint(40, 126)
#         password += chr(random_num)
#     return password
# def is_valid_password(password):
#     if len(password) != 8:
#         return False
#     has_islover = False
#     has_isdigit = False
#     has_isupper = False
#     for char in password:
#         print("char=", char)
#         if char.isdigit():
#             has_isdigit = True
#         elif char.islower():
#             has_islover = True
#         elif char.isupper():
#             has_isupper = True
#         print(has_isupper, has_islover, has_isdigit)
#         if has_isupper and has_islover and has_isdigit:
#             return True
#     return False
# def get_password():
#     for _ in range(100):
#         password = get_random_password()
#         print(f"is_valid_password({password}): ", is_valid_password(password))
#         if is_valid_password(password):
#             print(f"password({password}): True")
#             return password
#     return None
# get_password()

# def parse_folder1(path):
#     files = []
#     folders = []
#     # Перевіряємо, чи шлях існує та чи є це директорія
#     if path.exists() and path.is_dir():
#         # Проходимось по об'єктам у директорії
#         for item in path.iterdir():
#             # Перевіряємо, чи це файл
#             if item.is_file():
#                 files.append(item.name)
#             # Перевіряємо, чи це директорія
#             elif item.is_dir():
#                 folders.append(item.name)
#     return files, folders
# def parse_folder(path):
#     files = []
#     folders = []
#     if path.exists() and path.is_dir():
#         for item in path.iterdir():
#             if item.is_file():
#                 files.append(item.name)
#             elif item.is_dir():
#                 folders.append(item.name)
#     return files, folders
# # Приклад використання:
# directory_path = Path('/шлях/до/директорії')  # Замініть шлях на потрібний вам
# files, folders = parse_folder(directory_path)
# print("Список файлів:", files)
# print("Список директорій:", folders)

# def parse_args1():
#     # Відсікаємо перший аргумент, оскільки він є назвою скрипта
#     arguments = sys.argv[1:]
#     # Повертаємо аргументи, об'єднані пробілами
#     return ' '.join(arguments)
# # Приклад використання:
# args_string = parse_args()
# print("Аргументи командного рядка:", args_string)

# def real_len(input_string):
#     # Створюємо множину керівних символів, які потрібно видалити
#     control_chars = set('\n\f\r\t\v')
#     # Використовуємо генератор списку для створення рядка без керівних символів
#     cleaned_string = ''.join(
#         char for char in input_string if char not in control_chars)
#     # Повертаємо довжину очищеного рядка
#     return len(cleaned_string)
# # Приклад використання:
# string1 = 'Alex\nKdfe23\t\f\v.\r'
# string2 = 'Al\nKdfe23\t\v.\r'
# length1 = real_len(string1)
# length2 = real_len(string2)
# print("Довжина першого рядка без керівних символів:", length1)
# print("Довжина другого рядка без керівних символів:", length2)

# def sanitize_phone_number1(phone_number):
#     # Використовуємо регулярний вираз для вилучення лише цифр
#     normalized_number = re.sub(r'\D', '', phone_number)
#     normalized_number = normalized_number.strip()
#     # print("normalized_number: " + normalized_number)

#     # Перевіряємо, чи номер починається з '380' (український міжнародний код)
#     if normalized_number.startswith('380') and len(normalized_number) == 12:
#         return normalized_number
#     # Якщо не відповідає українському формату, перевіряємо, чи номер має 10 цифр
#     # elif len(normalized_number) == 10:
#     #     return '380' + normalized_number
#     else:
#         return None  # Повертаємо None у випадку неправильного формату
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone
# # Приклади використання функції
# phone_numbers = [
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]
# for phone in phone_numbers:
#     sanitized_number = sanitize_phone_number(phone)
#     if sanitized_number:
#         print(sanitized_number)
#     else:
#         print(f"Неправильний номер: {phone}")


# def is_check_name(fullname, first_name):
#     # Перевіряємо, чи рядок fullname починається з рядка first_name з урахуванням регістру
#     return fullname.startswith(first_name)
# # Приклади використання функції
# fullname = "John Doe"
# first_name1 = "John"
# first_name2 = "jOhn"
# first_name3 = "Jane"
# # True, так як "John Doe" починається з "John"
# print(is_check_name(fullname, first_name1))
# # False, так як регістр не співпадає
# print(is_check_name(fullname, first_name2))
# # False, так як "John Doe" не починається з "Jane"
# print(is_check_name(fullname, first_name3))

# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

# def get_phone_numbers_for_countries(list_phones):
#     country_numbers = {"UA": [], "JP": [], "SG": [], "TW": [], }

#     for phone_number in list_phones:
#         sanitized_number = sanitize_phone_number(phone_number)
#         if sanitized_number:
#             if sanitized_number.startswith("380"):
#                 country_numbers["UA"].append(sanitized_number)
#             elif sanitized_number.startswith("81"):
#                 country_numbers["JP"].append(sanitized_number)
#             elif sanitized_number.startswith("65"):
#                 country_numbers["SG"].append(sanitized_number)
#             elif sanitized_number.startswith("886"):
#                 country_numbers["TW"].append(sanitized_number)
#             else:
#                 country_numbers["UA"].append(sanitized_number)
#     return country_numbers

# # Приклад використання функції
# phone_numbers = [
#     "+38(050)123-32-34",
#     "0503451234",
#     "+65(050)8889900",
#     "886050-111-22-22",
#     "38050 111 22 11",
#     "8133456789",  # Приклад номеру для якого не вказана країна
# ]
# result = get_phone_numbers_for_countries(phone_numbers)
# print(result)

# def is_spam_words(text, spam_words, space_around=False):
#     text = text.lower()
#     for word in spam_words:
#         if space_around:
#             if ' ' + word + ' ' in text or ' ' + word + '.' in text or ' ' + word in text:
#                 return True
#         elif word in text:
#             return True
#     return False
# Приклади використання функції
# spam_words = ["лох"]
# Приклади зі спеціально вказаними пробілами
# print(is_spam_words("Молох", spam_words))  # True
# print(is_spam_words("Молох", spam_words, True))  # False
# print(is_spam_words("Ты лох.", spam_words))  # True
# print(is_spam_words("Ты лох.", spam_words, True))  # True

# # Приклад без пробілів (простий пошук)
# print(is_spam_words("Тыл охочо ", spam_words))  # True
# print(is_spam_words("Тыл охочо ", spam_words))  # True
# print(is_spam_words("Тыл охочо лох.", spam_words, True))  # False
# print(is_spam_words('Ты хорош, но выглядишь как лох.', ['лох'], True))  # True
# print(is_spam_words('Молох бог ужасен.', ['лох'], True))  # False

# CYRILLIC = ("а", "ч", "ш")
# LATIN = ("a", "ch", "sh")
# TRANSLIT_DICT = {}
# for c, l in zip(CYRILLIC, LATIN):
#     TRANSLIT_DICT[ord(c)] = l
#     TRANSLIT_DICT[ord(c.upper())] = l.upper()
# print("TRANSLIT_DICT", TRANSLIT_DICT)
# print("чаша".translate(TRANSLIT_DICT))  # chasha
# print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA

# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
# TRANS = {}
# for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c)] = l
#     TRANS[ord(c.upper())] = l.upper()
# def translate(name):
#     name = name.translate(TRANS)
#     return name
# Приклад використання функції
# print(translate("Дмитро Короб"))  # Dmitro Korob
# print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk

# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
# def formatted_grades(students):
#     global grades
#     formatted_list = []
#     # Заголовок таблиці
#     header = f"{'No':>4}|{'Name':<10}|{'Grade':^5}|{'Score':^5}"
#     formatted_list.append(header)
#     # Ініціалізуємо лічильник для нумерації студентів
#     count = 1
#     for name, grade in students.items():
#         # Форматуємо рядок для кожного студента
#         formatted_row = f"{count:>4}|{name:<10}|{grade:^5}|{grades[grade]:^5}"
#         formatted_list.append(formatted_row)
#         count += 1
#     return formatted_list
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# # Виводимо таблицю
# for line in formatted_grades(students):
#     print(line)

# def formatted_numbers():
#     formatted_list = []
#     header = f"|{'decimal':^10}|{'hex':^10}|{'binary':>10}|"
#     # separator = f"|{'-'*10}|{'-'*10}|{'-'*10}|"
#     formatted_list.extend([header])
#     for decimal in range(16):
#         hex_value = format(decimal, 'x')
#         binary_value = format(decimal, 'b')
#         formatted_row = f"|{decimal:<10}|{hex_value:^10}|{binary_value:>10}|"
#         formatted_list.append(formatted_row)
#     return formatted_list
# # Виводимо таблицю
# for line in formatted_numbers():
#     print(line)

# def find_word(text, word):
#     result = {}
#     result["search_string"] = word
#     result["string"] = text
#     # Виконуємо пошук слова у тексті
#     search_result = text.find(word)
#     if search_result != -1:
#         result["result"] = True
#         result["first_index"] = search_result
#         result["last_index"] = search_result + len(word)
#     else:
#         result["result"] = False
#         result["first_index"] = None
#         result["last_index"] = None
#     return result
# Приклади використання функції
# text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
# Знайдено слово "Python"
# print(find_word(text, "Python"))
# Спроба знайти слово "python" (регістронезалежний пошук)
# print(find_word(text, "python"))


# def find_all_words(text, word):
#     pattern = re.compile(f'\\b{re.escape(word)}\\b', re.IGNORECASE)
#     matches = pattern.finditer(text)
#     result = []
#     for match in matches:
#         result.append(match.group())
#     return result
# # Приклад використання функції
# text = "Python is a widely used programming language. python is versatile and easy to learn. PYTHON is powerful."
# word = "python"
# matches = find_all_words(text, word)
# print(matches)


# def replace_spam_words(text, spam_words):
#     for word in spam_words:
#         pattern = re.compile(re.escape(word), re.IGNORECASE)

#         replacement = '*' * len(word)

#         text = pattern.sub(replacement, text)

#     return text
# Приклад використання функції
# text = "This is a sample text with some bad words like Spam and ViAgRa."
# spam_words = ["spam", "viagra"]
# result_text = replace_spam_words(text, spam_words)
# print(result_text)

# def find_all_emails(text):
# regex = r"[a-zA-Z]{1}[\w\.]+@[a-zA-z]+\.[a-zA-Z]{2,}"
#     result = re.findall(
#         r'[A-Za-z][A-Za-z0-9_.]+@[A-Za-z]+\.[A-Za-z]{2,}', text)
#     return result

# Приклад використання функції
# text = 'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'
# text3 = 'cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com'
#      'cool@api.io', 'first.middle.last@iana.or', 'a2@test.com', 'a3@test.com'
#      'Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com'
# emails = find_all_emails(text)
# print(emails)
# def find_all_phones(text):
#     result = re.findall(r"(\+380\(\d{2}\)\d{3}-\d{2}-\d{2}|\+380\(\d{2}\)\d{3}-\d{1}-\d{3})", text)
#     return result

# def find_all_links(text):
#     result = []
#     iterator = re.finditer(r"(https|http)?://[A-Za-z0-9_-]+(\.[A-Za-z0-9_-]+)+[A-Za-z0-9_.-]+", text)
#     for match in iterator:
#         result.append(match.group())
#     return result

# def total_salary(path):
#     # Відкриваємо файл за вказаним шляхом для читання
#     file = open(path, 'r')
#     # Ініціалізуємо змінну для суми
#     total = 0.0
#     # Читаємо файл рядок за рядком
#     line = file.readline()
#     while line:
#         # Розділяємо рядок на ім'я розробника та заробітну плату
#         parts = line.strip().split(',')
#         # Перевіряємо, чи правильно розділено рядок
#         if len(parts) == 2:
#             try:
#                 # Додаємо заробітну плату розробника до загальної суми
#                 salary = float(parts[1])
#                 total += salary
#             except ValueError:
#                 # Якщо не вдалося перетворити заробітну плату в число, ігноруємо рядок
#                 pass
#         # Читаємо наступний рядок
#         line = file.readline()
#     # Закриваємо файл
#     file.close()
#     return total
# Приклад використання функції
# path = "salary_data.txt"
# total = total_salary(path)
# print("Загальна сума заробітної плати:", total)

# def write_employees_to_file(employee_list, path):
#     # Відкриваємо файл для запису у режимі "w"
#     file = open(path, 'w')

#     # Проходимося по списку відділів і списку співробітників у кожному відділі
#     for department in employee_list:
#         for employee in department:
#             # Записуємо дані про співробітника в файл та додаємо символ нового рядка
#             file.write(employee + '\n')

#     # Закриваємо файл
#     file.close()

# # Приклад використання функції
# employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# path = 'employees.txt'
# write_employees_to_file(employee_list, path)

# def read_employees_from_file(path):
#     # Відкриваємо файл для читання у режимі "r"
#     file = open(path, 'r')
#     # Ініціалізуємо список для зберігання співробітників
#     employees = []
#     # Прочитуємо файл рядок за рядком
#     for line in file:
#         # Видаляємо символ нового рядка (\n) та додаємо рядок до списку співробітників
#         employees.append(line.strip())
#     # Закриваємо файл
#     file.close()
#     # Повертаємо список співробітників
#     return employees
# # Приклад використання функції
# path = 'employees.txt'
# employee_list = read_employees_from_file(path)
# print(employee_list)

# def add_employee_to_file(record, path):
#     # Відкриваємо файл для додавання у режимі 'a'
#     file = open(path, 'a')

#     # Додаємо запис про співробітника у файл та додаємо символ нового рядка
#     file.write(record + '\n')

#     # Закриваємо файл
#     file.close()

# # Приклад використання функції
# record = 'Drake Mikelsson,19'
# path = 'employees.txt'
# add_employee_to_file(record, path)

# def get_cats_info(path):
#     cat_list = []

#     with open(path, 'r') as file:
#         for line in file:
#             parts = line.strip().split(',')
#             if len(parts) == 3:
#                 cat_info = {
#                     "id": parts[0],
#                     "name": parts[1],
#                     "age": parts[2]
#                 }
#                 cat_list.append(cat_info)

#     return cat_list

# # Приклад використання функції з вашим файлом
# file_path = 'your_file.txt'
# cats = get_cats_info(file_path)
# for cat in cats:
#     print(cat)

# def get_recipe(path, search_id):
#     with open(path, 'r') as file:
#         for line in file:
#             parts = line.strip().split(',')
#             if len(parts) >= 3 and parts[0] == search_id:
#                 recipe_info = {
#                     "id": parts[0],
#                     "name": parts[1],
#                     "ingredients": parts[2:]
#                 }
#                 return recipe_info

#     # Якщо рецепта з зазначеним search_id не знайдено, повертаємо None
#     return None

# # Приклад використання функції з вашим файлом і search_id
# file_path = 'your_file.txt'
# search_id = "60b90c3b13067a15887e1ae4"
# recipe = get_recipe(file_path, search_id)

# if recipe is not None:
#     print(recipe)
# else:
#     print("Рецепт не знайдено.")

# def sanitize_file(source, output):
#     with open(source, 'r') as source_file, open(output, 'w') as output_file:
#         for line in source_file:
#             cleaned_line = ''.join(char for char in line if not char.isdigit())
#             output_file.write(cleaned_line)

# # Приклад використання функції
# source_file_path = 'source.txt'
# output_file_path = 'output.txt'
# sanitize_file(source_file_path, output_file_path)

# def save_applicant_data(source, output):
#     with open(output, 'w') as output_file:
#         for applicant in source:
#             applicant_data = [
#                 applicant["name"],
#                 str(applicant["specialty"]),
#                 str(applicant["math"]),
#                 str(applicant["lang"]),
#                 str(applicant["eng"])
#             ]
#             output_line = ','.join(applicant_data) + '\n'
#             output_file.write(output_line)

# # Приклад використання функції
# applicant_list = [
#     {
#         "name": "Kovalchuk Oleksiy",
#         "specialty": 301,
#         "math": 175,
#         "lang": 180,
#         "eng": 155,
#     },
#     {
#         "name": "Ivanchuk Boryslav",
#         "specialty": 101,
#         "math": 135,
#         "lang": 150,
#         "eng": 165,
#     },
#     {
#         "name": "Karpenko Dmitro",
#         "specialty": 201,
#         "math": 155,
#         "lang": 175,
#         "eng": 185,
#     },
# ]

# output_file_path = 'output.txt'
# save_applicant_data(applicant_list, output_file_path)

# def is_equal_string(utf8_string, utf16_string):
#     print("utf8_string: ", utf8_string)
#     print("utf16_string: ", utf16_string)
#     utf8_str = utf8_string.decode("utf-8")
#     utf16_str = utf16_string.decode("utf-16")
#     print("utf8_string2: ", utf8_str)
#     print("utf16_string2: ", utf16_str)
#     dfre_str = "Привіт, світе!".encode()
#     print("byte_str", dfre_str)
#     # Порівнюємо рядки, перетворені до спільного кодування
#     return utf8_str == utf16_str
# # Приклад використання функції
# utf8_str = "Привіт, світе!".encode("utf-8")
# utf16_str = "Привіт, світе!".encode("utf-16")
# result = is_equal_string(utf8_str, utf16_str)
# print(result)  # Повинно вивести True

# def save_credentials_users(path, users_info):
#     with open(path, 'wb') as file:
#         for username, password in users_info.items():
#             user_data = f"{username}:{password}\n"
#             file.write(user_data.encode("utf-8"))

# # Приклад використання функції зі словником користувачів та шляхом до файлу
# user_credentials = {
#     'andry': 'uyro18890D',
#     'steve': 'oppjM13LL9e',
# }

# file_path = 'users_credentials.txt'
# save_credentials_users(file_path, user_credentials)


# def encode_data_to_base64(data):
#     encoded_data = []
#     for item in data:
#         # Розділяємо пару username:password та кодуємо у формат Base64
#         encoded_item = base64.b64encode(item.encode("utf-8")).decode("utf-8")
#         res = "Привіт, світе!".encode("utf-8")
#         print("encoded utf-8", res)
#         res = base64.b64encode(
#             "Привіт, світе!".encode("utf-8"))
#         print("base64.b64encode", res)
#         res = base64.b64encode(
#             "Привіт, світе!".encode("utf-8")).decode("utf-8")
#         print("base64.b64encode-decoded utf-8", res)
#         encoded_data.append(encoded_item)
#     return encoded_data
# # Приклад використання функції зі списком username:password
# data_list = ['andry:uyro18890D', 'steve:oppjM13LL9e']
# encoded_data = encode_data_to_base64(data_list)
# print(encoded_data)


# def create_backup(path, file_name, employee_residence):
#     # Створюємо бінарний файл з ім'ям file_name у теку path
#     with open((path + '/' + file_name), 'wb') as file:
#         for employee, residence in employee_residence.items():
#             data = f"{employee} {residence}\n"
#             file.write(data.encode("utf-8"))
#     archive_name = shutil.make_archive(
#         'backup_folder', 'zip', path)
#     return archive_name
# # Приклад використання функції зі словником та шляхом
# employee_residence = {'Michael': 'Canada', 'John': 'USA', 'Liza': 'Australia'}
# # Замініть на шлях до папки, де потрібно створити бекап
# path_to_backup = 'c:/Users/CFC/Desktop/GoItHomeWork/Python/Backup/Backup_folder'
# backup_file_path = create_backup(
#     path_to_backup, 'backup.txt', employee_residence)
# print("Шлях до архіву бекапу:", backup_file_path)
# def unpack(archive_path, path_to_unpack):
#     shutil.unpack_archive(archive_path, path_to_unpack)
# # Приклад використання функції зі шляхом до архіву та шляхом для розпакування
# # Замініть на шлях до архіву
# archive_path = 'c:/Users/CFC/Desktop/GoItHomeWork/Python/backup_folder.zip'
# # Замініть на шлях, куди потрібно розпакувати архів
# path_to_unpack = 'c:/Users/CFC/Desktop/GoItHomeWork/Python/Backup/'
# unpack(archive_path, path_to_unpack)


# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)  # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})
# print(mark_counts.most_common(1))  # [(4, 4)]
# print(mark_counts.most_common(5))  # [(4, 4), (6, 3), (1, 3), (2, 2)]

# from setuptools import setup
# def do_setup(args_dict, requires, entry_points):
#     args_dict["install_requires"] = requires
#     args_dict["entry_points"] = entry_points
#     # setup(**args_dict)
#     setup(name=args_dict['name'],
#           version=args_dict['version'],
#           description=args_dict['description'],
#           url=args_dict['url'],
#           author=args_dict['author'],
#           author_email=args_dict['author_email'],
#           license=args_dict['license'],
#           packages=args_dict['packages'],
#           install_requires=args_dict["install_requires"],
#           entry_points=args_dict["entry_points"],
#           )

# def is_integer1(s):
#     # Видаляємо початкові та кінцеві прогалини з рядка
#     s = s.strip()
#     # Якщо рядок залишився пустим після видалення прогалин, повертаємо False
#     if len(s) == 0:
#         return False
#     # Перевіряємо, чи є перший символ "+" або "-"
#     if s[0] in ('+', '-'):
#         # Якщо так, перевіряємо, що за ними йдуть цифри
#         return s[1:].isdigit()
#     else:
#         # Якщо перший символ не "+", не "-", перевіряємо, що весь рядок складається з цифр
#         return s.isdigit()

# def is_integer(s):
#     s = s.strip()
#     if len(s) == 0:
#         return False
#     if s[0] in ["+", "-"]:
#         return s[1:].isdigit()
#     else:
#         return s.isdigit()
# # Приклад використання:
# s1 = "12345"     # Повинно повернути True
# s2 = "-42"       # Повинно повернути True
# s3 = "3.14"      # Повинно повернути False
# # Повинно повернути True (після видалення прогалин "567" є цілим числом)
# s4 = "  567  "
# s5 = " +567 "
# print(f"s1:{s1}", is_integer(s1))
# print(f"s2:{s2}", is_integer(s2))
# print(f"s3:{s3}", is_integer(s3))
# print(f"s4:{s4}", is_integer(s4))
# print(f"s5:{s5}", is_integer(s5))

# def capital_text1(input_text):
#     # Розділяємо текст на речення за допомогою крапок, знаків оклику та питання
#     # sentences = re.split(r'(\.|\?|!)\s*', input_text) # бьє перед знаками !|?|.|
#     sentences = re.split(r'(?<=[.!?])\s*', input_text)
#     # Перетворюємо перший символ кожного речення у велику літеру
#     for i in range(len(sentences)):
#         sentence = sentences[i].strip()  # не потрібно
#         if len(sentence) > 0:
#             sentences[i] = sentence[0].upper() + sentence[1:]
#     result = ' '.join(sentences)
#     return result

# import re
# def capital_text(input_text):
#     sentences = re.split(r'(?<=[.!?])\s+', input_text)
#     for i in range(len(sentences)):
#         print(f"{i}", sentences[i])
#         sentences[i] = sentences[i].capitalize()

#     result = ' '.join(sentences)
#     return result
# Приклад використання:
# input_text = "це речення. це інше речення! і ще одне речення? так зване. або не так зване! але це точно."
# print(capital_text(input_text))

# text = "Це речення. Це інше речення! І ще одне речення? Так зване. Або не так зване! Але це точно."
# # Розділяємо текст на речення за допомогою крапок, знаків оклику та питання
# sentences = re.split(r'(?<=[.!?])\s+', text)
# # Виводимо розділені речення
# for sentence in sentences:
#     print(sentence)

# def solve_riddle(riddle, word_length, start_letter, reverse=False):
#      # Якщо reverse=False, шукаємо слово в прямому порядку
#     if reverse:
#         riddle = riddle[::-1]
#     for i in range(len(riddle) - word_length + 1):
#         if riddle[i] == start_letter:
#             potential_word = riddle[i:i+word_length]
#             return potential_word
#     return ""
# # Приклад використання:
# # riddle = "rewopretmi1"
# riddle = "1imterpower"
# word_length = 5
# start_letter = "p"
# found_word = solve_riddle(riddle, word_length, start_letter, reverse=0)
# print(found_word)  # Виведе "power"

# def data_preparation(list_data):
#     combined_data = []
#     for sublist in list_data:
#         if len(sublist) > 2:
#             sublist.remove(max(sublist))
#             sublist.remove(min(sublist))
#         combined_data.extend(sublist)
#     combined_data.sort(reverse=True)
#     return combined_data
# # Приклад використання функції
# list_data = [[1, 2, 3], [3, 4], [5, 6]]
# result = data_preparation(list_data)
# print(result)  # Результат: [6, 5, 4, 3, 2]


# def tokenize_expression(expression):
#     # Визначаємо регулярний вираз для пошуку чисел, операторів та дужок
#     pattern = r'\d+|[\+\-\*/()]'

#     # Використовуємо регулярний вираз для знаходження всіх лексем
#     tokens = re.findall(pattern, expression)

#     # Видаляємо прогалини із списку лексем
#     tokens = [token.strip() for token in tokens if token.strip() != '']

#     return tokens
# # Приклад використання функції
# expression = "2+ (34-5) * 3"
# tokens = tokenize_expression(expression)
# print(tokens)  # Результат: ['2', '+', '34', '-', '5', '*', '3']

# def all_sub_lists(data):
#     sublists = [[]]
#     for j in range(1, len(data) + 1):
#         for i in range(len(data)):
#             print(
#                 f"data[i={i}, j={j}] data[{i}]={data[i]} data[{i}:{j}]",  data[i:j])
#             sublists.append(data[i:j])
#             j = j + 1
#             if j == len(data) + 1:
#                 break
#     return sublists
# my_list = [4, 6, 1, 3]
# result = all_sub_lists(my_list)
# print("[[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]")
# print(result)
# [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]].
# `data[i:j]` - це зріз (slice) списку, який включає елементи з індексу `i` (включно) до індексу `j` (не включно).
#  В інших словах, це підсписок списку, який містить усі елементи з початкового списку з індексами від `i` до `j-1`.
# Наприклад, якщо `data = [1, 2, 3, 4, 5]`, і ми використовуємо `data[1:4]`, то отримаємо зріз `[2, 3, 4]`,
#  оскільки він включає елементи з індексами 1, 2 і 3 (індекс 4 не включено).
# Приклад використання функції

# def make_request(keys, values):
#     # Перевірка, чи довжина списків keys і values збігається
#     if len(keys) != len(values):
#         return {}  # Повертаємо порожній словник у разі несоответствия довжин
#     # Створюємо словник, використовуючи функцію zip для збігання ключів та значень
#     request = dict(zip(keys, values))
#     return request
# # Приклад використання функції
# keys = ["name", "age", "city", "state", "country"]
# values = ["John", 30, "New York"]
# request = make_request(keys, values)
# print(request)

# def sequence_buttons1(string):
#     button_map = {
#         '1': '.,?!:',
#         '2': 'ABC',
#         '3': 'DEF',
#         '4': 'GHI',
#         '5': 'JKL',
#         '6': 'MNO',
#         '7': 'PQRS',
#         '8': 'TUV',
#         '9': 'WXYZ',
#         '0': ' '
#     }
#     string = string.upper()
#     sequence = ""
#     prev_button = None
#     for char in string:
#         found = False
#         for button, chars in button_map.items():
#             if char in chars:
#                 # Якщо символ знайдено в поточній кнопці, додаємо відповідну послідовність кнопок
#                 # if button == prev_button:
#                 #     print(f"{button}chars=", chars)
#                 #     print(f"chars.index({char}) + 1={chars.index(char)+1}")
#                 sequence += button * (chars.index(char) + 1)
#                 # prev_button = button
#                 found = True
#                 break
#         if not found:
#             # Якщо символ не знайдено в жодній кнопці, ігноруємо його
#             pass
#     return sequence

# def sequence_buttons(string):
#     button_map = {
#         '1': '.,?!:',
#         '2': 'ABC',
#         '3': 'DEF',
#         '4': 'GHI',
#         '5': 'JKL',
#         '6': 'MNO',
#         '7': 'PQRS',
#         '8': 'TUV',
#         '9': 'WXYZ',
#         '0': ' '
#     }
#     string = string.upper()
#     sequence = ""
#     for char in string:
#         for button, chars in button_map.items():
#             if char in chars:
#                 sequence += button * (chars.index(char) + 1)
#                 break
#     return sequence
# # Приклад використання функції
# text = "Hello, World!"
# result = sequence_buttons(text)
# print("4433555555666110966677755531111")
# print(result)  # Результат: "4433555555666110966677755531111"

# def file_operations(path, additional_info, start_pos, count_chars):
#     try:
#         with open(path, 'a+') as file:
#             # Додаємо додаткову інформацію до кінця файлу
#             file.write(additional_info)

#             # Переходимо на початок файлу
#             file.seek(0)

#             # Зчитуємо рядок з позиції start_pos завдовжки count_chars
#             file.seek(start_pos)
#             result = file.read(count_chars)

#             return result
#     except FileNotFoundError:
#         return "File not found"
#     except Exception as e:
#         return str(e)

# def file_operations(path, additional_info, start_pos, count_chars):
#     try:
#         # Відкриваємо файл для додавання інформації (режим "a")
#         with open(path, 'a') as file:
#             # Додаємо додаткову інформацію до кінця файлу
#             file.write(additional_info)

#         # Відкриваємо файл для читання (режим "r")
#         with open(path, 'r') as file:
#             # Переходимо на початок файлу
#             file.seek(start_pos)

#             # Зчитуємо рядок з позиції start_pos завдовжки count_chars
#             result = file.read(count_chars)

#             return result
#     except FileNotFoundError:
#         return "File not found"
#     except Exception as e:
#         return str(e)


# Приклад використання функції
# path = "example.txt"
# additional_info = "This is additional information."
# start_pos = 10
# count_chars = 20

# result = file_operations(path, additional_info, start_pos, count_chars)
# print(result)


# # Приклад використання функції
# path = "example.txt"
# additional_info = "This is additional information."
# start_pos = 10
# count_chars = 20

# result = file_operations(path, additional_info, start_pos, count_chars)
# print(result)

# def get_employees_by_profession(path, profession):
#     try:
#         found_employees = []  # Список для збереження імен співробітників з певною професією
#         with open(path, 'r') as file:
#             lines = file.readlines()  # Отримуємо всі рядки з файлу

#         # Проходимося по кожному рядку та перевіряємо, чи містить професію
#         for line in lines:
#             if profession in line:
#                 # parts = line.split()  # Розділяємо рядок на слова
#                 if len(line) > 1:
#                     # Додаємо ім'я співробітника до списку
#                     print(
#                         f'line.replace(profession, ""):{line.replace(profession, "").strip()}:')
#                     found_employees.append(
#                         line.replace(profession, "").strip())

#         # Об'єднуємо імена знайдених співробітників в один рядок з пробілами
#         result = ' '.join(found_employees)

#         return result
#     except FileNotFoundError:
#         return "File not found"
#     except Exception as e:
#         return str(e)


# print(get_employees_by_profession("./users.txt", "cook"))

# Приклад використання функції
# path = "employees.txt"
# profession = "cook"
# result = get_employees_by_profession(path, profession)
# print(result)

# def is_valid_pin_codes(pin_codes):
#     print("pin_codes: ", pin_codes)
#     if not pin_codes:
#         return False
#     unique_pin_codes = set()
#     for pin_code in pin_codes:
#         if len(pin_code) != 4:
#             return False
#         if not pin_code.isdigit():
#             return False
#         unique_pin_codes.add(pin_code)
#         print("unique_pin_codes: ", unique_pin_codes)
#     if len(unique_pin_codes) == len(pin_codes):
#         return True
#     else:
#         return False
# pin_codes = ['1101', '9034', '0011']
# is_valid_pin_codes(pin_codes)

# def parse_input(user_input):
#     cmd, *args = user_input.split()
#     cmd = cmd.strip().lower()
#     return cmd, *args
# def add_contact(args, contacts):
#     name, phone = args
#     contacts[name] = phone
#     return "Contact added."
# def main():
#     contacts = {}
#     print("Welcome to the assistant bot!")
#     while True:
#         user_input = input("Enter a command: ")
#         command, *args = parse_input(user_input)
#         if command in ["close", "exit"]:
#             print("Good bye!")
#             break
#         elif command == "hello":
#             print("How can I help you?")
#         if len(args) != 2:
#             print("Invalid args.")
#             continue
#         if not args[1].isdigit():
#             print("Invalid number phone.")
#             continue
#         elif command == "add":
#             print(add_contact(args, contacts))
#             print("Contacts:", contacts)
#         else:
#             print("Invalid command.")
# if __name__ == "__main__":
#     main()

# from datetime import datetime, timedelta
# from collections import defaultdict
# def get_birthdays_per_week(users):
#     birthday_dict = defaultdict(list)
#     today = datetime.today().date()
#     print("today:", today)
#     next_week_start = today + timedelta(days=(7 - today.weekday()))
#     print(
#         f"next_week_start {next_week_start} days=(7 - today.weekday()={today.weekday()}")
#     next_week_end = next_week_start + timedelta(days=7)
#     for user in users:
#         name = user["name"]
#         birthday = user["birthday"].date()
#         birthday_this_year = birthday.replace(year=today.year)
#         if birthday_this_year < today:
#             # Якщо так, розглядаємо дату на наступний рік
#             birthday_this_year = birthday_this_year.replace(
#                 year=today.year + 1)
#         # Визначаємо різницю між днем народження і поточним днем
#         delta_days = (birthday_this_year - today).days
#         birthday_weekday = (today.weekday() + delta_days) % 7 # 0 - понеділок, 6 - неділя
#         if next_week_start <= birthday_this_year < next_week_end:
#             if birthday_weekday == 5 or birthday_weekday == 6:
#                 birthday_weekday = 0
#             day_of_week = get_day_of_week(birthday_weekday)
#             birthday_dict[day_of_week].append(name)
#     # Визначаємо порядок днів тижня від понеділка до п'ятниці
#     sorted_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#     for day in sorted_days:
#         names = birthday_dict[day]
#         if names:
#             print(f"{day}: {', '.join(names)}")
# def get_day_of_week(weekday):
#     days = ["Monday", "Tuesday", "Wednesday",
#             "Thursday", "Friday", "Saturday", "Sunday"]
#     return days[weekday]
# # Приклад використання:
# users = [
#     {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
#     {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
#     {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
#     {"name": "Dmitry Lupherov", "birthday": datetime(1980, 10, 20)},
#     {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
# ]
# get_birthdays_per_week(users)

# from datetime import datetime, timedelta
# from collections import defaultdict
# def get_birthdays_per_week1(users):
#     birthday_dict = defaultdict(list)
#     today = datetime.today().date()  # без часу тільки дата
#     next_week_start = today + timedelta(days=(7 - today.weekday()))
#     print("next_week_start", next_week_start)
#     next_week_end = next_week_start + timedelta(days=7)
#     print("next_week_end", next_week_end)
#     for user in users:
#         name = user["name"]
#         birthday = user["birthday"].date()
#         birthday_this_year = birthday.replace(year=today.year)
#         print("birthday_this_year=", birthday_this_year)
#         if birthday_this_year < today:
#             # Якщо так, розглядаємо дату на наступний рік
#             birthday_this_year = birthday_this_year.replace(
#                 year=today.year + 1)
#         delta_days = (birthday_this_year - today).days
#         print("delta_days = ", delta_days)
#         birthday_weekday = (today.weekday() + delta_days) % 7 # 0 - понеділок, 6 - неділя
#         if next_week_start <= birthday_this_year < next_week_end:
#             if birthday_weekday == 5 or birthday_weekday == 6:
#                 birthday_weekday = 0 # Якщо це вихідний, привітаємо в понеділок
#             day_of_week = get_day_of_week(birthday_weekday)
#             birthday_dict[day_of_week].append(name)
#     print("birthday_dict", birthday_dict)
#     for day, names in birthday_dict.items():
#         if names:
#             print(f"{day}: {', '.join(names)}")  # Виводимо результат
# def get_day_of_week(weekday):
#     days = ["Monday", "Tuesday", "Wednesday",
#             "Thursday", "Friday", "Saturday", "Sunday"]
#     return days[weekday]
# users = [
#     {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
#     {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
#     {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 29)},
#     {"name": "Dmitry Lupherov", "birthday": datetime(1980, 10, 23)},
#     {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
# ]
# get_birthdays_per_week1(users)

# def to_indexed(source_file, output_file):
#     try:
#         with open(source_file, 'r') as source:
#             lines = source.readlines()
#     except FileNotFoundError:
#         print(f"File '{source_file}' not found.")
#         return
#     with open(output_file, 'w') as output:
#         for i, line in enumerate(lines):
#             indexed_line = f"{i}: {line}"
#             output.write(indexed_line)
#     print(
#         f"Файл '{output_file}' успішно створено і заповнено з номерами рядків.")

# def flatten(data):
#     if not data:
#         return []
#     # Якщо перший елемент списку є списком
#     if isinstance(data[0], list):
#         first = flatten(data[0])
#         rest = flatten(data[1:])
#         return first + rest
#     else:
#         # Якщо перший елемент списку не є списком
#         # Отримуємо перший список із першого елемента списку
#         first = [data[0]]
#         # Рекурсивно викликаємо функцію з рештою списку без першого елемента
#         rest = flatten(data[1:])
#         # Повертаємо конкатенацію двох списків
#         return first + rest
# # Приклад використання:
# data = [1, [2], [3, 4, [5, 6]], 7]
# result = flatten(data)
# print(result)  # Виведе [1, 2, 3, 4, 5, 6, 7]

# def decode(data):
#     decoded_list = []  # Починаємо з порожнього списку для розшифрованих значень
#     i = 0  # Індекс, що вказує на поточний елемент у закодованому списку
#     while i < len(data):
#         if i + 1 < len(data) and isinstance(data[i + 1], int):
#             # Якщо наступний елемент є цілим числом (лічильником)
#             # Додаємо поточне значення до розшифрованого списку у кількість разів, яку вказує лічильник
#             decoded_list.extend([data[i]] * data[i + 1])
#             i += 2  # Переходимо до наступного незакодованого значення
#         else:
#             # Якщо наступний елемент не є цілим числом (лічильником)
#             # Додаємо поточне значення до розшифрованого списку один раз
#             decoded_list.append(data[i])
#             i += 1  # Переходимо до наступного незакодованого значення
#     return decoded_list
# # Приклад використання:
# data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
# decoded_list = decode(data)
# # Виведе ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
# print(decoded_list)


# def decode(data):
#     def decode_recursive(data, index):
#         if index >= len(data):
#             return []

#         current_element = data[index]
#         if isinstance(current_element, int):
#             return [data[index - 1]] * current_element + decode_recursive(data, index + 1)
#         else:
#             return [current_element] + decode_recursive(data, index + 1)

#     return decode_recursive(data, 0)


# # Приклад використання:
# data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
# decoded_list = decode(data)
# # Виведе ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
# print(decoded_list)

# def decode(data):
#     def decode_recursive(data, index):
#         # Базовий випадок: якщо індекс перевищує довжину закодованого списку,
#         #  завершуємо рекурсію
#         if index >= len(data):
#             return []
#         current_element = data[index]
#         if isinstance(current_element, int):
#             # Якщо поточний елемент є цілим числом (лічильником)
#             # Додаємо поточне значення до розшифрованого списку у кількість разів,
#             #  яку вказує лічильник
#             return [data[index - 1]] * (current_element - 1) + decode_recursive(data, index + 1)
#         else:
#             # Якщо поточний елемент не є цілим числом (лічильником)
#             # Додаємо поточне значення до розшифрованого списку один раз
#             return [current_element] + decode_recursive(data, index + 1)
#     return decode_recursive(data, 0)


# # Приклад використання:
# data1 = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
# data = ['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]
# decoded_list = decode(data)
# # Виведе ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
# # Виведе ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
# print(decoded_list)

# def encode(input_list):
#     def encode_recursive(input_list, current_value, count):
#         if not input_list:
#             # Базовий випадок: якщо вхідний список порожній, завершуємо рекурсію
#             return []

#         current_element = input_list[0]

#         if current_element == current_value:
#             # Якщо поточний елемент дорівнює поточному значенню
#             # Збільшуємо лічильник повторів
#             count += 1
#         else:
#             # Якщо поточний елемент відрізняється від поточного значення
#             # Додаємо поточне значення та лічильник повторів до закодованого списку
#             result = [current_value, count]
#             # Рекурсивно викликаємо функцію з рештою списку та новим поточним значенням та лічильником
#             result.extend(encode_recursive(input_list[1:], current_element, 1))
#             return result

#         # Рекурсивно викликаємо функцію з рештою списку та поточним значенням та лічильником
#         return encode_recursive(input_list[1:], current_value, count)

#     if not input_list:
#         return []

#     # Початкове значення та лічильник для першого елемента
#     current_value = input_list[0]
#     count = 1

#     return encode_recursive(input_list[1:], current_value, count)


# # Приклад використання:
# input_list = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
# encoded_list = encode(input_list)
# print(encoded_list)  # Виведе ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

# def encode(data):
#     if not data:
#         return []

#     def encode_recursive(data, current_value, count):
#         if not data:
#             # print("No data to encode", current_value, count)
#             return [current_value, count]
#         current_element = data[0]
#         # print(f"current_element = {data[0]}")
#         if current_element == current_value:
#             # Якщо поточний елемент дорівнює поточному значенню
#             # Збільшуємо лічильник повторів
#             count += 1
#             # print(f"current_element {current_value} == current_value",
#             #       "count =", count)
#         else:
#             # Якщо поточний елемент відрізняється від поточного значення
#             # Додаємо поточне значення та лічильник повторів до закодованого списку
#             result = [current_value, count]
#             # Рекурсивно викликаємо функцію з рештою списку та новим поточним значенням та лічильником
#             print("result1:", result)
#             # print(
#             #     f"encode_(data[1:]={data[1:]}, {current_element}, 1)")
#             result.extend(encode_recursive(data[1:], current_element, 1))
#             print("extend:", encode_recursive(
#                 data[1:], current_element, 1))
#             print("result.extended:", result)
#             return result

#         # print("encode_data3[1:]:", data[1:], current_value, count)
#         # Рекурсивно викликаємо функцію з рештою списку та поточним значенням та лічильником
#         return encode_recursive(data[1:], current_value, count)

#     # Початкове значення та лічильник для першого елемента
#     current_value = data[0]
#     count = 1
#     # print("data0[1:]", data[1:], "Current0=", current_value, "count0=", count)
#     return encode_recursive(data[1:], current_value, count)
# # Приклад використання:
# data = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
# # data = []
# encoded_list = encode(data)
# print(encoded_list)  # Виведе ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

# from datetime import datetime
# def get_days_from_today(date):
#     # Перетворюємо вхідну рядок у об'єкт datetime, без часу тільки дата
#     input_date = datetime.strptime(date, "%Y-%m-%d").date()
#     print("input date=", input_date)
#     today = datetime.today().date()  # без часу тільки дата
#     print("today=", today)
#     delta_days = (today - input_date).days  # Обчислюємо різницю в днях
#     print("delta days=", delta_days)
#     return delta_days

# # Приклад використання:
# # current_date = datetime.now().strftime("%Y-%m-%d")
# current_date = datetime.now().date()  # без часу тільки дата
# date_to_compare = "2021-10-09"
# days_difference = get_days_from_today(date_to_compare)
# print(f"Поточна дата: {current_date}")
# print(
#     f"Різниця в днях між поточною датою і {date_to_compare}: {days_difference}")
# def get_days_in_month(month, year):
#     # Перевірка на коректність вхідних даних
#     if month < 1 or month > 12:
#         return "Номер місяця має бути у діапазоні від 1 до 12."
#     if year < 0 or len(str(year)) != 4:
#         return "Рік має складатися із чотирьох цифр."
#     # Список місяців, який враховує кількість днів у кожному місяці
#     days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     # Перевірка, чи рік є високосним
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         # Якщо рік високосний, то лютого 29 днів
#         days_in_month[1] = 29
#     # Повертаємо кількість днів для заданого місяця
#     return days_in_month[month - 1]
# # Приклад використання функції
# month = 2
# year = 2024  # Приклад високосного року
# days = get_days_in_month(month, year)
# print(f"У місяці {month} року {year} {days} днів.")

# from datetime import datetime


# def get_str_date(date):
#     # Перетворюємо вхідний рядок у об'єкт datetime
#     date_format = '%Y-%m-%d %H:%M:%S.%fZ'
#     date_obj = datetime.strptime(date, date_format)

#     # Форматуємо об'єкт datetime у рядок бажаного формату
#     formatted_date = date_obj.strftime('%A %d %B %Y')

#     return formatted_date


# # Приклад використання
# date = '2021-05-27 17:08:34.149Z'
# formatted_date = get_str_date(date)
# print(formatted_date)  # Виведе 'Thursday 27 May 2021'

# import random
# def get_numbers_ticket(min, max, quantity):
#     # Перевірка на допустимість вхідних параметрів
#     if min < 1 or max > 1000 or min >= max or quantity <= min or quantity >= max:
#         return []
#     # Створення списку усіх можливих чисел у діапазоні
#     possible_numbers = list(range(min, max + 1))
#     # Вибір випадкових чисел без дублікатів
#     selected_numbers = random.sample(possible_numbers, quantity)
#     # Сортування вибраних чисел та повернення результату
#     selected_numbers.sort()
#     return selected_numbers
# # Приклад виклику функції з діапазоном від 1 до 49 і кількістю чисел 6
# numbers = get_numbers_ticket(1, 49, 6)
# print(numbers)

# from random import randrange
# def get_numbers_ticket(min, max, quantity):
#     # Перевірка на допустимість вхідних параметрів
#     if min < 1 or max > 1000 or min >= max or quantity <= min or quantity >= max:
#         return []
#     selected_numbers = set()  # Використовуємо множину для унікальних чисел
#     while len(selected_numbers) < quantity:
#         # Генеруємо випадкове число в діапазоні
#         random_number = random.randrange(min, max + 1)
#         selected_numbers.add(random_number)  # Додаємо у множину
#     # Повертаємо список відсортованих унікальних чисел
#     return sorted(list(selected_numbers))
# # Приклад виклику функції з діапазоном від 1 до 49 і кількістю чисел 6
# numbers = get_numbers_ticket(1, 49, 6)
# print(numbers)

# import random


# def get_random_winners(quantity, participants):
#     # Отримайте список ключів і перетворіть його в список
#     participant_keys = list(participants.keys())

#     # Перемішайте список ключів
#     random.shuffle(participant_keys)

#     # Перевірте, чи передана кількість переможців більша за загальну кількість користувачів
#     if quantity > len(participant_keys):
#         return []

#     # Виберіть випадкових переможців
#     winners = random.sample(participant_keys, k = quantity)

#     return winners
# # Приклад виклику функції
# participants = {
#     "603d2cec9993c627f0982404": "test@test.com",
#     "603f79022922882d30dd7bb6": "test11@test.com",
#     "60577ce4b536f8259cc225d2": "test2@test.com",
#     "605884760742316c07eae603": "vitanlhouse@gmail.com",
#     "605b89080c318d66862db390": "elhe2013@gmail.com",
# }
# winners = get_random_winners(2, participants)
# print(winners)

# from decimal import Decimal, getcontext
# def decimal_average(number_list, signs_count):
#     # Встановлюємо контекст для чисел типу Decimal
#     # +1 для збереження точності при обчисленні середнього
#     getcontext().prec = signs_count
#     # Перетворюємо всі числа у списку на Decimal
#     decimal_numbers = [Decimal(str(num)) for num in number_list]
#     # Обчислюємо середнє арифметичне
#     total = sum(decimal_numbers)
#     average = total / len(decimal_numbers)
#     return average
# print(decimal_average([3, 5, 77, 23, 0.57], 6))
# print(decimal_average([31, 55, 177, 2300, 1.57], 9))
# print(decimal_average(
#     [4.5788689699797, 34.7576578697964, 86.8877666656633, 12], 6))

# from collections import namedtuple

# # Оголошення іменованого кортежу Cat
# Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])


# def convert_list(cats):
#     # Перевіряємо, чи вхідний параметр є списком іменованих кортежів (Cat)
#     if isinstance(cats, list) and all(isinstance(cat, Cat) for cat in cats):
#         # Якщо це список іменованих кортежів, конвертуємо його в список словників
#         return [{'nickname': cat.nickname, 'age': cat.age, 'owner': cat.owner} for cat in cats]
#     # Перевіряємо, чи вхідний параметр є списком словників
#     elif isinstance(cats, list) and all(isinstance(cat, dict) for cat in cats):
#         # Якщо це список словників, конвертуємо його в список іменованих кортежів
#         return [Cat(cat['nickname'], cat['age'], cat['owner']) for cat in cats]
#     else:
#         # Якщо тип не відповідає ні списку іменованих кортежів, ні списку словників, повертаємо порожній список
#         return []


# # Приклад використання
# cats_namedtuple = [Cat("Mick", 5, "Sara"), Cat(
#     "Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# cats_dict = [
#     {"nickname": "Mick", "age": 5, "owner": "Sara"},
#     {"nickname": "Barsik", "age": 7, "owner": "Olga"},
#     {"nickname": "Simon", "age": 3, "owner": "Yura"}
# ]

# result_dict = convert_list(cats_namedtuple)
# print(result_dict)

# result_namedtuple = convert_list(cats_dict)
# print(result_namedtuple)

# from collections import Counter

# # Список IP адрес
# IP = [
#     "85.157.172.253",
#     "85.157.172.253",
#     "66.50.38.43",
#     "66.50.38.43",
#     "66.50.38.43",
#     "66.50.38.43",
#     "123.45.67.89",
#     "123.45.67.89",
#     "55.66.77.88",
# ]

# # Функція для підрахунку кількості входжень кожного IP-адреси


# def get_count_visits_from_ip(ips):
#     ip_counts = Counter(ips)
#     return dict(ip_counts)

# # Функція для знаходження найбільш часто вживаного IP-адреси та кількості його появ в списку


# def get_frequent_visit_from_ip(ips):
#     ip_counts = Counter(ips)
#     most_common_ip = ip_counts.most_common(1)
#     return most_common_ip[0]


# # Виклик функцій і виведення результатів
# ip_counts = get_count_visits_from_ip(IP)
# most_common_ip = get_frequent_visit_from_ip(IP)

# print("Кількість входжень кожного IP-адреси:")
# print(ip_counts)

# print("\nНайбільш часто вживаний IP-адрес та кількість його появ в списку:")
# print(most_common_ip)

# from collections import deque

# MAX_LEN = 10  # Задайте бажаний максимальний розмір LIFO


# class LIFO:
#     def __init__(self):
#         self.lifo = deque(maxlen=MAX_LEN)

#     def push(self, element):
#         self.lifo.appendleft(element)

#     def pop(self):
#         if len(self.lifo) > 0:
#             return self.lifo.popleft()
#         else:
#             return None  # Повертаємо None, якщо LIFO пустий


# lifo = deque(maxlen=MAX_LEN)
# def push(element):
#     return lifo.appendleft(element)
# def pop():
#     if len(lifo) > 0:
#         return lifo.popleft()
#     else:
#         return None
# Створення екземпляру LIFO
# lifo = LIFO()

# # Додавання елементів до LIFO
# lifo.push(1)
# lifo.push(2)
# lifo.push(3)

# # Дістаємо та виводимо елементи з LIFO
# print(lifo.pop())  # Виведе 3
# print(lifo.pop())  # Виведе 2
# print(lifo.pop())  # Виведе 1
# print(lifo.pop())  # Виведе None, так як LIFO порожній

# from collections import deque


# class FIFO:
#     def __init__(self, max_len):
#         self.fifo = deque()
#         self.max_len = max_len

#     def push(self, element):
#         if len(self.fifo) < self.max_len:
#             self.fifo.append(element)
#         else:
#             print("FIFO is full. Cannot push element.")

#     def pop(self):
#         if len(self.fifo) > 0:
#             return self.fifo.popleft()
#         else:
#             print("FIFO is empty. Cannot pop element.")
#             return None


# # Визначте максимальну довжину черги
# MAX_LEN = 5


# def push(element):
#     if len(fifo) < MAX_LEN:
#         fifo.append(element)
#     else:
#         print("FIFO is full. Cannot push element.")


# def pop(self):
#     if len(fifo) > 0:
#         return fifo.popleft()
#     else:
#         print("FIFO is empty. Cannot pop element.")
#         return None


# # Створення FIFO
# fifo = FIFO(MAX_LEN)

# # Додавання елементів до черги
# fifo.push(1)
# fifo.push(2)
# fifo.push(3)
# fifo.push(4)
# fifo.push(5)

# # Спроба додати ще один елемент, коли черга вже повна
# fifo.push(6)

# # Витягнення та виведення елементів з черги
# print(fifo.pop())  # Виведе 1
# print(fifo.pop())  # Виведе 2
# print(fifo.pop())  # Виведе 3
# print(fifo.pop())  # Виведе 4
# print(fifo.pop())  # Виведе 5

# # Спроба витягнути елемент, коли черга вже пуста
# print(fifo.pop())  # Виведе "FIFO is empty. Cannot pop element."

# def get_student_grade(option):
#     grades = {
#         'F': 1,
#         'FX': 2,
#         'E': 3,
#         'D': 3,
#         'C': 4,
#         'B': 5,
#         'A': 5,
#     }
#     descriptions = {
#         'F': 'Unsatisfactorily',
#         'FX': 'Unsatisfactorily',
#         'E': 'Enough',
#         'D': 'Satisfactorily',
#         'C': 'Good',
#         'B': 'Very good',
#         'A': 'Perfectly',
#     }

#     def get_grade(key):
#         return grades.get(key, None)

#     def get_description(key):
#         return descriptions.get(key, None)

#     if option == 'grade':
#         return get_grade
#     elif option == 'description':
#         return get_description
#     else:
#         return None


# # Приклад використання:
# grade_function = get_student_grade('grade')
# description_function = get_student_grade('description')

# grade = grade_function('E')  # Поверне 3
# description = description_function('E')  # Поверне 'Enough'
# invalid_option = get_student_grade('invalid_option')  # Поверне None

# DEFAULT_DISCOUNT = 0.1  # Глобальна змінна для знижки за відсутності discount у клієнта


# def get_discount_price_customer(price, customer):

#     discount = customer.get("discount", DEFAULT_DISCOUNT)

#     discounted_price = price * (1 - discount)

#     return discounted_price


# # Приклад використання функції:
# customer1 = {"name": "Dima"}
# customer2 = {"name": "Boris", "discount": 0.15}
# product_price = 100.0

# discounted_price1 = get_discount_price_customer(product_price, customer1)
# discounted_price2 = get_discount_price_customer(product_price, customer2)

# print(f"Ціна для клієнта Dima: {discounted_price1}")
# print(f"Ціна для клієнта Boris: {discounted_price2}")

# def caching_fibonacci():
#     cache = {}

#     def fibonacci(n):
#         if n in cache:
#             return cache[n]

#         if n <= 1:
#             result = n
#         else:
#             result = fibonacci(n - 1) + fibonacci(n - 2)

#         cache[n] = result
#         print("cache: ", cache)
#         return result

#     return fibonacci


# # Приклад використання:
# fib = caching_fibonacci()
# print(fib(-5))  # Виведе -5
# # print(fib(10))  # Виведе 55

# def discount_price(discount):
#     def calculate_discounted_price(price):
#         discounted_price = price - (price * discount)
#         return discounted_price

#     return calculate_discounted_price


# # Приклад використання:
# cost_15 = discount_price(0.15)
# cost_10 = discount_price(0.10)
# cost_05 = discount_price(0.05)

# price = 100
# print(cost_15(price))  # Виведе 85.0
# print(cost_10(price))  # Виведе 90.0
# print(cost_05(price))  # Виведе 95.0

# def format_phone_number(sanitize_func):
#     def wrapper(phone_number):
#         normalized_number = sanitize_func(phone_number)

#         if len(normalized_number) == 10:
#             formatted_number = "+38" + normalized_number
#         else:
#             formatted_number = "+" + normalized_number

#         return formatted_number

#     return wrapper

# # Оригінальна функція sanitize_phone_number


# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone

# # Приклад використання декоратора


# @format_phone_number
# def sanitized_and_formatted_phone_number(phone_number):
#     return sanitize_phone_number(phone_number)


# # Приклади використання
# print(sanitized_and_formatted_phone_number("0501234567"))  # +380501234567
# print(sanitized_and_formatted_phone_number("380501234567"))  # +380501234567
# print(sanitized_and_formatted_phone_number("+380501234567"))  # +380501234567

# import re
# def generator_numbers(string=""):
#     # Використовуємо регулярний вираз для знаходження всіх цілих чисел у рядку
#     pattern = r'\d+'
#     matches = re.finditer(pattern, string)
#     # Ітеруємося по знайдених числах і видаємо їх
#     for match in matches:
#         yield int(match.group())
# def sum_profit(string):
#     total_profit = 0
#     # Використовуємо generator_numbers для отримання чисел з рядка
#     for number in generator_numbers(string):
#         total_profit += number
#     return total_profit
# string = "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
# result = sum_profit(string)
# print("Total profit:", result)

# def generator_numbers(string=""):
#     current_number = ""
#     for char in string:
#         if char.isdigit():
#             current_number += char
#         elif current_number:
#             yield int(current_number)
#             current_number = ""
#     if current_number:
#         yield int(current_number)


# def sum_profit(string):
#     total_profit = 0

#     # Використовуємо generator_numbers для отримання чисел з рядка
#     for number in generator_numbers(string):
#         total_profit += number

#     return total_profit

numbers = [1, 2, 3, 4, 5]

# for i in map(lambda x: x ** 2, numbers):
#     print(i)
# for i in map(lambda x: x ** 2, numbers):
#     print(i)


# def normal_name(list_name):

#     def capitalize_first_letter(word):
#         return word.capitalize()

#     capitalized_names = list(map(capitalize_first_letter, list_name))

#     return capitalized_names


# name = ["dan", "jane", "steve", "mike"]
# result = normal_name(name)
# print(result)

# def get_emails(list_contacts):
#     # Використовуємо функцію генератор map до i_го словника контакту
#     emails = map(lambda contact: contact['email'], list_contacts)
#     email_list = []
#     for i in emails:
#         email_list.append(i)
#         print("email_list", email_list)

#     # Перетворюємо результат map в список
#     # email_list = list("547")

#     return email_list


# # Приклад використання:
# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     {
#         "name": "John Smith",
#         "email": "john.smith@example.com",
#         "phone": "(123) 456-7890",
#         "favorite": True,
#     }
# ]

# email_list = get_emails(contacts)
# print(email_list)

# for i in filter(lambda x: (x + 1) % 2, range(1, 10 + 1)):
#     print(i)
# some_str = 'aaAbbB C F DDd EEe'
# for i in filter(lambda x: x.isupper(), some_str):
#     print(i)
# upper_list = list(filter(lambda x: x.isupper(), some_str))
# print("upper_list", upper_list)

# payment = [100, -3, 400, 35, -100]
# def positive_values(list_payment):
#     pos_list = list(filter(lambda x: x > 0, list_payment))
#     return pos_list
# print("pos_list", positive_values(payment))


# def get_favorites(contacts):
#     favorites_list = list(
#         filter(lambda contact: contact["favorite"], contacts))
#     return favorites_list
# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": True,
#     }
# ]
# print("favorites", get_favorites(contacts))
# def get_favorites(contacts):
#     # Використовуємо функцію filter для відфільтрування обраних контактів
#     favorite_contacts = filter(lambda contact: contact['favorite'], contacts)
#     # Перетворюємо результат filter в список
#     favorite_contacts_list = list(favorite_contacts)
#     return favorite_contacts_list
# Приклад використання:
# contacts = [
#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     },
#     {
#         "name": "John Smith",
#         "email": "john.smith@example.com",
#         "phone": "(123) 456-7890",
#         "favorite": True,
#     },
#     {
#         "name": "Jane Doe",
#         "email": "jane.doe@example.com",
#         "phone": "(987) 654-3210",
#         "favorite": True,
#     }
# ]

# favorite_contacts = get_favorites(contacts)
# print(favorite_contacts)


# def sum_numbers(numbers):
#     result = reduce((lambda x, y: x + y), numbers, 0)
#     return result


# numbers = [3, 4, 6, 9, 34, 12]
# print(sum_numbers(numbers))  # 10

# payment = [100, -3, 400, 35, -100]


# def amount_payment(payment):
#     pos_list = list(filter(lambda x: x > 0, payment))
#     result = reduce((lambda x, y: x + y), pos_list, 0)
#     return result


# print("pay=", amount_payment(payment))
