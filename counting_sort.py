def counting_sort(arr):
    # Знайдемо максимальний та мінімальний елементи у масиві
    max_element = max(arr)
    min_element = min(arr)
    
    # Визначимо розмір масиву підрахунку та ініціалізуємо його нулями
    count = [0] * (max_element - min_element + 1)
    
    # Підрахунок кількості входжень кожного елемента
    for num in arr:
        count[num - min_element] += 1
    
    # Акумуляція кількостей
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Побудова відсортованого масиву
    result = [0] * len(arr)
    for num in reversed(arr):
        result[count[num - min_element] - 1] = num
        count[num - min_element] -= 1
    
    return result

# Приклад використання
input_array = [4, 2, 2, 8, 3, 3, 1]
sorted_array = counting_sort(input_array)
print("Вхідний масив:", input_array)
print("Відсортований масив:", sorted_array)
