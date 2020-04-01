"""
Сравните две одинаковых буквы,
но одна из них должна быть заглавной, при помощи операторов сравнения ">"
и выведите результат на экран.
Выведите на экран ASCII код каждой из букв
"""

first_value = 'W'
second_value = 'w'

print(first_value > second_value)
print(first_value < second_value)
print(first_value >= second_value)
print(first_value <= second_value)
print(first_value == second_value)
print(first_value != second_value)
print(f'ASCII code \'{first_value}\'\tis\t{ord(first_value)}')
print(f'ASCII \'{second_value}\'\tis\t{ord(first_value)}')
