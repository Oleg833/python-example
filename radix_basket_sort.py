def radix_sort(arr):
    # Знайти максимальний елемент для визначення кількості розрядів
    max_num = max(arr)
    # Визначення кількості розрядів у максимальному числі
    num_digits = len(str(max_num))
    
    # Використовуємо Bucket Sort для кожного розряду
    for digit in range(num_digits):
        buckets = [[] for _ in range(10)]  # 10 ведер для десятичних цифр (0-9)
        
        # Розподіл елементів по відповідним ведрам
        for num in arr:
            # Отримати значення розряду за поточним індексом
            div1 = num // 10**digit
            exp1 = 10**digit
            print(f"num {num} // {exp1} (10**{digit}) = {div1}")
            bucket_index = (num // 10**digit) % 10
            print(f"{div1} % 10 = {bucket_index}")
            buckets[bucket_index].append(num)
        
        # Збирання відсортованих елементів
        arr2 = [el_arr for bucket in buckets for el_arr in bucket]
    
    return arr2

# Приклад використання
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(sorted_arr)
