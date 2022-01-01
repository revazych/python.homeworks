# class Cell:
#
#     def __init__(self, cell_num):
#         self.cell_num = cell_num
#
#     def __add__(self, other):
#         return Cell(self.cell_num + other.cell_num)
#
#     def __sub__(self, other):
#         result = self.cell_num - other.cell_num
#         if result <= 0:
#             return f"Разность меньше нуля"
#         return result
#
#     def __mul__(self, other):
#         return self.cell_num * other.cell_num
#
#     def __truediv__(self, other):
#         return self.cell_num / other.cell_num
#
#     def __int__(self, cell_parts):
#         self.cell_parts = cell_parts
#
#     def make_order(self, cell_parts):
#         k = ""
#         for el in range(self.cell_num // cell_parts):
#             k += '_' * cell_parts + '\n'
#         k += '_' * (self.cell_num % cell_parts) + '\n'
#         return k
#
#     def __str__(self):
#         return f'{self.cell_num}'
#
#
# cell_1 = Cell(22)
# cell_2 = Cell(12)
#
# print(Cell(cell_1))
# print(Cell(cell_2))
# print(cell_1 + cell_2)
# print(cell_1 - cell_2)
# print(cell_1 * cell_2)
# print(cell_1 / cell_2)
# print(cell_1.make_order(8))
# print(cell_2.make_order(5))
