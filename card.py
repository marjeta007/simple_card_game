import random

from faker import Faker

fake = Faker()


class Card:
    color_order = color_list = ('green', 'yellow', 'red')
    number_list = tuple(range(1, 10 + 1))

    def __init__(self, color=None, number=None):
        if color and color not in self.color_list:
            raise ValueError(f'Illegal color {color}. {", ".join([str(color) for color in self.color_list])}')
        if number and number not in self.number_list:
            raise ValueError(f'Illegal number {number}. {", ".join([str(number) for number in self.number_list])}')

        self.__color = color or random.choice(self.color_list)
        self.__number = number or random.choice(self.number_list)

    def card_value(self):
        # print(self.number)
        # print(1 + self.color_list.index(self.color))
        # print(self.number * (1 + self.color_list.index(self.color)))
        return self.number * (1 + self.color_list.index(self.color))

    @classmethod
    def full_deck(cls):
        return [Card(color=color, number=number) for color in cls.color_list for number in cls.number_list]

    @classmethod
    def set_color_order(cls, color_order=None):
        color_order = color_order or []
        for color in color_order:
            if color not in Card.color_list:
                raise ValueError(f'Illegal colors present in requested color order: {color_order}')
        for color in Card.color_order:
            if color not in color_order:
                color_order.append(color)
        cls.color_order = color_order

    def __str__(self):
        return f'{self.color} {self.number}'

    def __repr__(self):
        return f'{str(self.color)[0]}{self.number}'

    def __int__(self):
        return self.number

    def __hash__(self):
        return hash((self.color, self.number))

    # noinspection PyBroadException
    def __eq__(self, other):
        try:
            return (self.color, self.number) == (other.color, other.number)
        except Exception:
            return False

    def __gt__(self, other):
        if self.color == other.color:
            return self.number > other.number
        else:
            return self.color_order.index(self.color) > self.color_order.index(other.color)

    @property
    def number(self):
        return self.__number

    # @number.setter
    # def number(self, value):
    #     pass

    @property
    def color(self):
        return self.__color

    # @color.setter
    # def color(self, value):
    #     pass
