class Product:
    def __init__(self, price, id, quantity):
        if not isinstance(price, int) or not isinstance(id, int) or not isinstance(quantity, int):
            raise self.ProductError('Invalid type')
        self.__price = price
        self.__id = id
        self.__quantity = quantity

    class ProductError(Exception):
        pass

    def __repr__(self):
        return 'id: {}, price: {}, quantity: {}'.format(self.__id, self.__price, self.__quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise self.ProductError('Invalid type')
        self.__price = price

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise self.ProductError('Invalid type')
        self.__id = id

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise self.ProductError('Invalid type')
        self.__quantity = quantity

    def buy(self, count):
        if count > self.quantity or count < 0:
            raise self.ProductError('Invalid quantity')
        self.quantity -= count
