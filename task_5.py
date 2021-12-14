# def numbers_string(numbers, stop_sym):
#     nums = numbers.split(' ')
#     numbers_sum = 0
#     for i in nums:
#         if i == stop_sym:
#             break
#         numbers_sum += int(i)
#     return numbers_sum
#
#
# a = 0
# stop_symbol = '&'
# stop = False
#
# while stop != True:
#     input_user = input('Введите числа через пробел ')
#     a += numbers_string(input_user, stop_symbol)
#     stop = stop_symbol in input_user
#     print(f'Сумма равна {a}')
#
