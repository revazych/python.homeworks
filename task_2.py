# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#
#     @abstractmethod
#     def __init__(self):
#         pass
#
#
# class Coat(Clothes):
#
#     def __init__(self, coat):
#         self.coat = coat
#
#     @property
#     def fabric_consumption(self):
#         return self.coat / 6.5 + 0.5
#
#
# class Suit(Clothes):
#
#     def __init__(self, suit):
#         self.suit = suit
#
#     @property
#     def fabric_consumption(self):
#         return 2 * self.suit + 0.3
#
#
# coat = Coat(48)
# suit = Suit(1.8)
# print(f'Расход ткани на пальто {coat.fabric_consumption}')
# print(f'Расход ткани на костюм {suit.fabric_consumption}')
# print(f'Общий расход ткани {coat.fabric_consumption + suit.fabric_consumption}')
