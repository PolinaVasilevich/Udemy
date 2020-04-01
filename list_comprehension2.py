"""
Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
создайте новый список содержащий нечетные числа исходного списка.
Выведите новый список на печать.

Решите задание двумя способами - при помощи List Comprehension и без него.
"""

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list_1 = []

# the first way
for number in digits:
    if number % 2 != 0:
        new_list_1.append(number)
print(new_list_1)

# the second way
new_list_2 = [number for number in digits if number % 2 != 0]
print(new_list_2)
