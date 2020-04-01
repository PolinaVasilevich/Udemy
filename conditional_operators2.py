"""
Напишите код, который выводит сообщение:
'Enter an integer number'.
 Если было введено чётное число, должно выводиться сообщение: 'The number is even',
 если было введено нечётное число, должно выводиться сообщение 'The number is odd'
"""

number = int(input('Enter a integer number:\n'))

if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')
