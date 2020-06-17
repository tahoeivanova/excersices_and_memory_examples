'''
Пользователь вводит трехзначное число.
Программа должна сложить цифры, из которых состоит это число.
'''

input_number = int(input('Введите трехзначное число'))
sum_of_digits = 0
for i in range(3):
    last_digit = input_number%10
    sum_of_digits += last_digit
    input_number //= 10
print(sum_of_digits)
