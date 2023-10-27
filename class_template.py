# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

#     def change_color(self, color):
#         Animal.color = color


# class Owner:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def info(self):
#         return {
#             'name': self.name,
#             'age': self.age,
#             'address': self.address
#         }


# first_animal = Animal("Simon", 10)
# second_animal = Animal("Bibic", 13)
# second_animal.change_weight(12)
# second_animal.change_color("red")


# class Cat(Animal):
#     def __init__(self, name, weight):
#         super().__init__(name, weight)

#     def say(self):
#         return "Meow"


# # Створюємо екземпляр класу Cat з ім'ям "Simon" і вагою 10 одиниць
# cat = Cat("Simon", 10)


# class Dog(Animal):
#     def __init__(self, nickname, weight, breed, owner):
#         self.breed = breed
#         self.owner = owner
#         super().__init__(nickname, weight)

#     def say(self):
#         return "Woof"

#     def who_is_owner(self):
#         return self.owner.info()

# class Animal:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         pass


# class Cat(Animal):
#     def say(self):
#         return "Meow"


# class Dog(Animal):
#     def say(self):
#         return "Woof"

# class CatDog(Cat, Dog):

#     def info(self):
#         return f"{self.nickname}-{self.weight}"


# class DogCat(Dog, Cat):

#     def info(self):
#         return f"{self.nickname}-{self.weight}"

# from collections import UserDict


# class LookUpKeyDict(UserDict):
#     def lookup_key(self, value):
#         keys = []
#         for key, val in self.data.items():
#             if val == value:
#                 keys.append(key)
#         return keys


# # Приклад використання:
# my_dict = LookUpKeyDict()
# my_dict['a'] = 1
# my_dict['b'] = 2
# my_dict['c'] = 1

# result = my_dict.lookup_key(1)
# print(result)  # Виведе: ['a', 'c']

# from collections import UserList

# class AmountPaymentList(UserList):
#     def amount_payment(self):
#         total = 0
#         for value in self.data:
#             if value > 0:
#                 total += value
#         return total

# # Створення об'єкта класу AmountPaymentList зі списком payment
# payment = AmountPaymentList([1, -3, 4])

# # Виклик методу amount_payment для обчислення суми платежів
# total_payment = payment.amount_payment()

# print("Загальна сума платежів:", total_payment)

# from collections import UserString

# class NumberString(UserString):
#     def number_count(self):
#         # Ініціалізуємо лічильник цифр
#         digit_count = 0

#         # Перевіряємо кожен символ рядка
#         for char in self.data:
#             if char.isdigit():  # Перевіряємо, чи символ є цифрою
#                 digit_count += 1

#         return digit_count

# # Приклад використання класу NumberString:
# my_string = NumberString("Hello12345World")
# count = my_string.number_count()
# print("Кількість цифр у рядку:", count)

# class IDException(Exception):
#     pass

# def add_id(id_list, employee_id):
#     if employee_id.startswith('01'):
#         id_list.append(employee_id)
#         return id_list
#     else:
#         raise IDException("Employee ID must start with '01'")

# # Приклад використання:
# employee_ids = ['0101', '0123', '0345']
# try:
#     new_id = '1234'
#     updated_ids = add_id(employee_ids, new_id)
#     print("Updated IDs:", updated_ids)
# except IDException as e:
#     print("Error:", e)

# class Mammal:
#     phrase = ''

#     def voice(self):
#         return self.phrase


# class Dog(Mammal):
#     phrase = 'Bark!'


# class Cat(Mammal):
#     phrase = 'Meow!'


# class Chupakabra:
#     def voice(self):
#         return 'Whooooo!!!'


# class Recorder:
#     def record_animal(self, animal):
#         voice = animal.voice()
#         print(f'Recorded "{voice}"')


# r = Recorder()
# cat = Cat()
# dog = Dog()
# strange_animal = Chupakabra()

# r.record_animal(cat)  # Recorded "Meow!"
# r.record_animal(dog)  # Recorded "Bark!"
# r.record_animal(strange_animal)  # Recorded "Whooooo!!!"
# class Cat:
#     def say(self):
#         return "Meow"


# class CatDog:
#     def __init__(self):
#         self.cat = Cat()

#     def say(self):
#         return self.cat.say()
# class Cat:
#     def say(self):
#         return "Meow"


# class CatDog:
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight

#     def say(self):
#         return "Meow"

#     def change_weight(self, weight):
#         self.weight = weight


# # Приклад використання:
# catdog = CatDog()
# print(catdog.say())  # Виведе "Meow"

import copy
import pickle


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            "id": self.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(contact)
        self.current_id += 1

# Приклад використання класу Contacts
# contacts_manager = Contacts()
# contacts_manager.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# contacts_manager.add_contacts("John Doe", "(123) 456-7890", "john.doe@example.com", False)
# print(contacts_manager.list_contacts())


# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         contact = {
#             "id": self.current_id,
#             "name": name,
#             "phone": phone,
#             "email": email,
#             "favorite": favorite
#         }
#         self.contacts.append(contact)
#         self.current_id += 1

#     def get_contact_by_id(self, contact_id):
#         for contact in self.contacts:
#             if contact["id"] == contact_id:
#                 return contact
#         return None

# Приклад використання класу Contacts
# contacts_manager = Contacts()
# contacts_manager.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# contacts_manager.add_contacts("John Doe", "(123) 456-7890", "john.doe@example.com", False)
# contact = contacts_manager.get_contact_by_id(1)
# if contact:
#     print(contact)
# else:
#     print("Contact not found")

# class Contacts:
#     current_id = 1

#     def __init__(self):
#         self.contacts = []

#     def list_contacts(self):
#         return self.contacts

#     def add_contacts(self, name, phone, email, favorite):
#         contact = {
#             "id": self.current_id,
#             "name": name,
#             "phone": phone,
#             "email": email,
#             "favorite": favorite
#         }
#         self.contacts.append(contact)
#         self.current_id += 1

#     def get_contact_by_id(self, contact_id):
#         for contact in self.contacts:
#             if contact["id"] == contact_id:
#                 return contact
#         return None

#     def remove_contacts(self, contact_id):
#         for contact in self.contacts:
#             if contact["id"] == contact_id:
#                 self.contacts.remove(contact)
#                 return

# Приклад використання класу Contacts
# contacts_manager = Contacts()
# contacts_manager.add_contacts("Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)
# contacts_manager.add_contacts("John Doe", "(123) 456-7890", "john.doe@example.com", False)
# contacts_manager.remove_contacts(1)
# print(contacts_manager.list_contacts())
# from random import randrange
# class Point:
#     def __init__(self, x, y):
#         self.__x = None
#         self.__y = None
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if (type(x) == int) or (type(x) == float):
#             self.__x = x

#     @property
#     def y(self):
#         return self.__y

#     @y.setter
#     def y(self, y):
#         if (type(y) == int) or (type(y) == float):
#             self.__y = y

#     def __str__(self):
#         return f"Point({self.x},{self.y})"


# class Vector:
#     def __init__(self, coordinates: Point):
#         self.coordinates = coordinates

#     def __setitem__(self, index, value):
#         if index == 0:
#             self.coordinates.x = value
#         if index == 1:
#             self.coordinates.y = value

#     def __getitem__(self, index):
#         if index == 0:
#             return self.coordinates.x
#         if index == 1:
#             return self.coordinates.y

#     def __call__(self, value=None):
#         if value:
#             return self.coordinates.x * value, self.coordinates.y * value
#         return self.coordinates.x, self.coordinates.y

#     def __add__(self, vector):
#         x = self.coordinates.x + vector.coordinates.x
#         y = self.coordinates.y + vector.coordinates.y
#         return Vector(Point(x, y))

#     def __sub__(self, vector):
#         x = self.coordinates.x - vector.coordinates.x
#         y = self.coordinates.x - vector.coordinates.y
#         return Vector(Point(x, y))

#     def __mul__(self, vector):
#         x = self.coordinates.x * vector.coordinates.x
#         y = self.coordinates.y * vector.coordinates.y
#         return x + y

#     def len(self):
#         return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

#     def __str__(self):
#         return f"Vector({self.coordinates.x},{self.coordinates.y})"

#     def __eq__(self, vector):
#         return self.coordinates.x == vector.coordinates.x and self.coordinates.y == vector.coordinates.y

#     def __ne__(self, vector):
#         return self.coordinates.x != vector.coordinates.x or self.coordinates.y != vector.coordinates.y

#     def __lt__(self, vector):
#         return self.coordinates.x < vector.coordinates.x or self.coordinates.y < vector.coordinates.y

#     def __gt__(self, vector):
#         return self.coordinates.x > vector.coordinates.x and self.coordinates.y > vector.coordinates.y

#     def __le__(self, vector):
#         return self.coordinates.x <= vector.coordinates.x and self.coordinates.y <= vector.coordinates.y

#     def __ge__(self, vector):
#         return self.coordinates.x >= vector.coordinates.x and self.coordinates.y >= vector.coordinates.y


# class Iterable:
#     def __init__(self, max_vectors, max_points):
#         self.current_index = 0
#         self.vectors = []
#         self.max_points = max_points
#         for _ in range(max_vectors):
#             self.vectors.append(
#                 Vector(Point(randrange(0, max_points), randrange(0, max_points))))

#     def __next__(self):
#         if self.current_index < len(self.vectors):
#             result = self.vectors[self.current_index]
#             self.current_index += 1
#             return result
#         raise StopIteration


# class RandomVectors:
#     def __init__(self, max_vectors=10, max_points=50):
#         self.max_vectors = max_vectors
#         self.max_points = max_points

#     def __iter__(self):
#         return Iterable(self.max_vectors, self.max_points)


# class Person:
#     def __init__(self, name: str, email: str, phone: str, favorite: bool):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.favorite = favorite


# def __copy__(self):
#     copy_obj = Person('', '', '', False)
#     copy_obj.name = copy.copy(self.name)
#     copy_obj.email = copy.copy(self.email)
#     copy_obj.phone = copy.copy(self.phone)
#     copy_obj.favorite = copy.copy(self.favorite)
#     return copy_obj


# class Contacts:
#     def __init__(self, filename: str, contacts: list[Person] = None):
#         if contacts is None:
#             contacts = []
#         self.filename = filename
#         self.contacts = contacts
#         self.is_unpacking = False
#         self.count_save = 0

#     def save_to_file(self):
#         with open(self.filename, "wb") as file:
#             pickle.dump(self, file)

#     def read_from_file(self):
#         with open(self.filename, "rb") as file:
#             content = pickle.load(file)
#         return content

#     def __getstate__(self):
#         attributes = self.__dict__.copy()
#         attributes['count_save'] += 1

#         return attributes

#     def __setstate__(self, value):
#         self.__dict__ = value
#         self.is_unpacking = True

#     def __copy__(self):
#         copy_obj = Contacts('')
#         copy_obj.filename = copy.copy(self.filename)
#         copy_obj.contacts = copy.copy(self.contacts)
#         copy_obj.is_unpacking = copy.copy(self.is_unpacking)
#         copy_obj.count_save = copy.copy(self.count_save)
#         return copy_obj

#     def __deepcopy__(self, memo):
#         copy_obj = Contacts('')
#         memo[id(copy_obj)] = copy_obj
#         copy_obj.filename = copy.copy(self.filename)
#         copy_obj.contacts = copy.deepcopy(self.contacts)
#         copy_obj.is_unpacking = copy.copy(self.is_unpacking)
#         copy_obj.count_save = copy.copy(self.count_save)
#         return copy_obj
