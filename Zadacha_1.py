import random

# Количество элементов в массиве
n = 10

# Формируем массив случайных чисел от 0 до 1
array = [random.random() for _ in range(n)]

print("Массив:", array)

min_value = min(array)
max_value = max(array)
average_value = sum(array) / len(array)

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", average_value)