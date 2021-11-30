# number_1 = input('Введите число ')
# number_2 = input('Введите число ')
# number_3 = input('Введите число ')
# str_1 = input('Введите слово ')
# str_2 = input('Введите букву ')
#
# result = number_1, number_2, number_3, str_1, str_2
# print(result)
#

# number_1 = int(input('Введите время в секундах '))
# result_1 = number_1 // 3600
# result_2 = number_1 % 3600
# result_3 = result_2 // 60
# result_4 = result_2 % 60
#
# result_str = f'Точное время {result_1:02} : {result_3:02} : {result_4:02}'
#
# print(result_str)

# string_1 = input('Введите число ')
# string_2 = string_1 * 2
# string_3 = string_1 * 3
#
# result = int(string_1) + int(string_2) + int(string_3)
#
# print(result)
#

# a = int(input('Введите целое положительное число '))
# b = a % 10
# while a > 0 and b != 9:
#     c = a % 10
#     if c > b:
#         b = c
#     a = a // 10
#     if b == 9:
#         print(f'наибольшая цифра в числе {b}')
#         break
#     if a == 0:
#         print(f'наибольшая цифра в числе {c}')
#         break


# number_1 = int(input('Введите выручку фирмы '))
# number_2 = int(input('Введите издержки фирмы '))
# number_3 = number_1 - number_2
# result = int(number_3) / int(number_1)
# if number_1 > number_2 :
#     print('Фирма работеет с прибылью')
#     result_str = f'Рентабильность составила {result}'
#     print(result_str)
#     number_4 = int(input('Укажите число сотрудников '))
#     result_1 = number_3 / number_4
#     result_str1 = f'Прибыль на 1 сотрудника составила {result_1}'
#     print(result_str1)
# else:
#     print('Фирма работает в убыток')
#

# a = int(input('Введите первоначальное количество километров '))
# b = int(input('Введите целевое количество километров '))
# counter = 0
# while a < b:
#     a *= 1.1
#     print(a)
#     counter += 1
#     if a >= b:
#         string = f'Понадобится {counter} дней'
#         print(string)
#         break
#
