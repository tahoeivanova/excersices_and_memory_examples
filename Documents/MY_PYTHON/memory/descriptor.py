# get, set, delete

# bad example
'''
class Order:
    # __slots__ = ('name', 'price','quantity')
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sum(self):
        return self.price * self.quantity
'''
# better
'''
class Order:

    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self.__quantity = quantity

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if value<0:
            raise ValueError('Цена не должна быть отрицательной!')

    @property
    def quanitity(self):
        return self.__quantity

    @quanitity.setter
    def quantity(self, value):
        if value<0:
            raise ValueError('Количество не может быть отрицательным')


    def sum(self):
        return self._price * self.__quantity
'''

# the best
# Использование дескриптора

# класс дексриптора
class NonNegative:
    def __init__(self, value=0):
        self._value = 0
    # Метод __get__ срабатывает по запросу данного атрибута
    def __get__(self, instance, owner):
        return self._value
    # Метод __set__ отвечает за настройку (как @property)
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Отрицательное число! Ошибка')
        self._value = value

# Класс
class Order:
    # Определяем правило доступа к атрибутам
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sum(self):
        return self.price * self.quantity


if __name__ == '__main__':
    apple_order = Order('apple', 90, 2)
    print(apple_order.sum())

    apple_order.price = -100
    print(apple_order.sum())

