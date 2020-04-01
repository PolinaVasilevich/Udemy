"""
Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola']
создайте новый список содержащий вторую букву из каждой
строки исходного списка. Выведите новый список на печать.

Решите задание двумя способами - при помощи List Comprehension и без него.
"""

greetings = ['hello', 'hi', 'hey', 'hola']
new_list_1 = []
# This is the first way
for word in greetings:
    new_list_1.append(word[1])

print('This\'s result of the first way:\n{}'.format(new_list_1))

# This is the second way
new_list_2 = [word[1] for word in greetings]
print('This\'s result of the second way:\n{}'.format(new_list_2))
