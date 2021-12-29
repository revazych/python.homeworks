# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {'wage': wage, 'bonus': bonus}
#
#
# class Position(Worker):
#
#     def get_full_name(self):
#         return self.name, self.surname, self.position, self._income['wage'] + self._income['bonus']
#
#
# result = Position('Вася', 'Пупкин', 'cтарший помощник младшего дворника', 5000, 1000)
# print(f'Данные сотрудника: {result.get_full_name()}')
