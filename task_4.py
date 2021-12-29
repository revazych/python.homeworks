# class Car:
#
#     def __init__(self, speed, colour, name, is_police, direction):
#         self.speed = speed
#         self.colour = colour
#         self.name = name
#         self.is_police = is_police
#         self.direction = direction
#
#     def go(self):
#         return print('Автомобиль движется')
#
#     def stop(self):
#         return print('Автомобиль стоит')
#
#     def turn(self):
#         return print(f'направление движения {self.direction}')
#
#     def show_speed(self):
#         return print(f'текущая скорость автомобиля {self.speed}')
#
#
# class TownCar(Car):
#
#     def show_speed(self):
#         super().show_speed()
#         if self.speed > 60:
#             return print(f'Превышение скорости! {self.speed}')
#
#
# class WorkCar(Car):
#
#     def show_speed(self):
#         super().show_speed()
#         if self.speed > 40:
#             return print('Превышение скорости!')
#
#
# class SportCar(Car):
#     pass
#
#
# class PoliceCar(Car):
#
#     def show_class(self):
#         if True:
#             return print('Это полицейская машина')
#
#
# data = PoliceCar(65, 'black', 'porshe', False, 'вправо')
#
# print(data.show_class())
# print(data.show_speed())
# print(data.go())
# print(data.stop())
# print(data.turn())
