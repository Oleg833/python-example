import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(arr):
    if len(arr) > 20000:  # Обмеження розміру масиву
        # Використовуйте інший алгоритм сортування
        quick_sort(arr)
    else:
        # Використовуйте Insertion Sort
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


def tim_sort(arr):
    arr.sort()

# Генеруємо тестові дані різних розмірів
data_sizes = [10, 100, 1000, 10000, 20000, 100000]

algorithms = ["Merge Sort", "Insertion Sort", "Timsort"]


# Виведення заголовків таблиці
print(f"{'Algorithm':<15}{'Data Size':<15}{'Time (seconds)':<15}")

# Перебір по алгоритмах та розмірах вибірки
for algorithm in algorithms:
    for size in data_sizes:
        data = [random.randint(1, 1000) for _ in range(size)]

        # Вимірювання часу виконання для кожного алгоритму
        if algorithm == "Merge Sort":
            time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
        elif algorithm == "Insertion Sort":
            time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
        elif algorithm == "Timsort":
            time = timeit.timeit(lambda: tim_sort(data.copy()), number=1)

        # Виведення результатів
        print(f"{algorithm:<15}{size:<15}{time:<15.6f}")

print("The end of time measurement")