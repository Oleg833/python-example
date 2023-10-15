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
#                 parts = line.split()  # Розділяємо рядок на слова
#                 if len(parts) > 1:
#                     # Додаємо ім'я співробітника до списку
#                     found_employees.append(parts[0])

#         # Об'єднуємо імена знайдених співробітників в один рядок з пробілами
#         result = ' '.join(found_employees)

#         return result
#     except FileNotFoundError:
#         return "File not found"
#     except Exception as e:
#         return str(e)


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

from datetime import datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)
    today = datetime.today().date()
    print("today:", today)
    next_week_start = today + timedelta(days=(7 - today.weekday()))
    print(
        f"next_week_start {next_week_start} days=(7 - today.weekday()={today.weekday()}")
    next_week_end = next_week_start + timedelta(days=7)

    # Перебираємо користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Визначаємо дату народження на цей рік
        birthday_this_year = birthday.replace(year=today.year)

        # Перевіряємо, чи вже минув день народження цього року
        if birthday_this_year < today:
            # Якщо так, розглядаємо дату на наступний рік
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        # Визначаємо різницю між днем народження і поточним днем
        delta_days = (birthday_this_year - today).days

        # Визначаємо день тижня дня народження
        # 0 - понеділок, 6 - неділя
        birthday_weekday = (today.weekday() + delta_days) % 7

        # Перевіряємо, чи день народження потрапляє в наступний тиждень
        if next_week_start <= birthday_this_year < next_week_end:
            # Додаємо ім'я до відповідного дня народження
            if birthday_weekday == 5 or birthday_weekday == 6:
                # Якщо це вихідний, привітаємо в понеділок
                birthday_weekday = 0
            day_of_week = get_day_of_week(birthday_weekday)
            birthday_dict[day_of_week].append(name)

    # Визначаємо порядок днів тижня від понеділка до п'ятниці
    sorted_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    # Виводимо результат в порядку
    for day in sorted_days:
        names = birthday_dict[day]
        if names:
            print(f"{day}: {', '.join(names)}")


def get_day_of_week(weekday):
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday]


# Приклад використання:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Dmitry Lupherov", "birthday": datetime(1980, 10, 20)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
]
get_birthdays_per_week(users)


def get_birthdays_per_week1(users):
    # Створюємо словник для зберігання імен на днях тижня
    birthday_dict = defaultdict(list)

    # Отримуємо поточну дату
    today = datetime.today().date()

    # Визначаємо початок і кінець наступного тижня
    next_week_start = today + timedelta(days=(7 - today.weekday()))
    next_week_end = next_week_start + timedelta(days=7)

    # Перебираємо користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # Визначаємо дату народження на цей рік
        birthday_this_year = birthday.replace(year=today.year)
        print("birthday_this_year=", birthday_this_year)

        # Перевіряємо, чи вже минув день народження цього року
        if birthday_this_year < today:
            # Якщо так, розглядаємо дату на наступний рік
            birthday_this_year = birthday_this_year.replace(
                year=today.year + 1)

        # Визначаємо різницю між днем народження і поточним днем
        delta_days = (birthday_this_year - today).days
        print("delta_days = ", delta_days)

        # Визначаємо день тижня дня народження
        # 0 - понеділок, 6 - неділя
        birthday_weekday = (today.weekday() + delta_days) % 7

        # Перевіряємо, чи день народження потрапляє в наступний тиждень
        if next_week_start <= birthday_this_year < next_week_end:
            # Додаємо ім'я до відповідного дня народження
            if birthday_weekday == 5 or birthday_weekday == 6:
                # Якщо це вихідний, привітаємо в понеділок
                birthday_weekday = 0
            day_of_week = get_day_of_week(birthday_weekday)
            birthday_dict[day_of_week].append(name)

    # Виводимо результат
    for day, names in birthday_dict.items():
        if names:
            print(f"{day}: {', '.join(names)}")


def get_day_of_week(weekday):
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    return days[weekday]


users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Dmitry Lupherov", "birthday": datetime(1980, 10, 20)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
]
get_birthdays_per_week1(users)
