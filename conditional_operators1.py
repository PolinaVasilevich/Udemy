"""
Напишите код, который выводит сообщение: 'Enter any number'.
Если было введено число 7, должно выводиться сообщение:
'7 is a lucky number! Today is your lucky day!', если введено
 что-то другое - должно выводиться сообщение 'Thank you! Have a nice day!'
"""

number = int(input('Enter any number:\n'))

if number == 7:
    print('7 is lucky number! Today is your lucky day!')
else:
    print('Thank you! Have a nice day!')
