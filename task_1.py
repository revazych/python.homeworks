# from random import randint
#
#
# class Matrix:
#
#     def __init__(self, nums):
#         self.nums = nums
#
#     def __str__(self):
#         k = ''
#         for a in range(len(self.nums)):
#             for b in range(len(self.nums[a])):
#                 k += f'{self.nums[a][b]:02} '
#             k += '\n'
#         return k
#
#     def __add__(self, other):
#         summ = [[self.nums[a][b] + other.nums[a][b] for b in range(len(self.nums[a]))] for a in range(len(self.nums))]
#         return Matrix(summ)
#
#
# list_1 = [[randint(0, 99) for _ in range(0, 10)] for _ in range(0, 10)]
# list_2 = [[randint(0, 99) for _ in range(0, 10)] for _ in range(0, 10)]
#
# print(Matrix(list_1))
# print(Matrix(list_2))
# print(Matrix(list_1) + Matrix(list_2))
