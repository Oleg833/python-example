def radix_sort(arr):
    # Знаходимо максимальний розряд
    max_num = max(arr)
    exp = 1

    # Застосовуємо сортування для кожного розряду
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Рахуємо кількість елементів на кожному розряді
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Знаходимо позиції елементів в відсортованому масиві
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Заповнюємо вихідний масив відсортованими елементами
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Копіюємо відсортований масив назад у вихідний масив
    for i in range(n):
        arr[i] = output[i]

# Приклад використання
arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Відсортований масив:", arr)
