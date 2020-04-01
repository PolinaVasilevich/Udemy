"""
При помощи функции randint() из модуля  random генерируйте числа
в диапазоне от 1 до 10 и помещайте в список,
до тех пор пока не будет сгенерировано число 7.
Распечатайте содержимое списка.
"""

from random import randint

number = 0
numbers_list = []

while number != 7:
    number = randint(1, 10)
    numbers_list.append(number)

print(numbers_list)
