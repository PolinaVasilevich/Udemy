"""
Используйте цикл for для вычисления суммы всех чётных чисел в диапазоне
от 10 до 30 (включая крайние значения). Выведите результат на печать
"""

number_sum = 0

for number in range(10, 31, 2):
    number_sum += number

print(number_sum)
