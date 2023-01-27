class Money:
    exchange = {'AMD': 1, 'RUB': 5.8, 'USD': 400, 'EUR': 430}

    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def __repr__(self):
        return '{} {}'.format(self.amount, self.currency)

    class MoneyError(Exception):
        pass

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if amount < 0 and not isinstance(amount, int):
            raise self.MoneyError('Money cannot be negative and should be an integer')
        self.__amount = amount

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, currency):
        if currency not in Money.exchange and not isinstance(currency, str):
            raise self.MoneyError('Currency should be a string')
        self.__amount = self.conversion(currency)
        self.__currency = currency

    def conversion(self, currency):
        if currency not in self.exchange:
            raise self.MoneyError("Invalid Currency")
        if self.currency == currency:
            return self.amount
        else:
            return round(self.amount * self.exchange[self.currency] / self.exchange[currency])

    def __add__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            answer = self.amount + other.amount
        elif isinstance(other, Money):
            answer = self.amount + other.conversion(self.currency)
        else:
            raise self.MoneyError("Object is not an instance of Money class")
        return Money(answer, self.currency)

    def __sub__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            answer = self.amount - other.amount
        elif isinstance(other, Money):
            answer = self.amount - other.conversion(self.currency)
        else:
            raise self.MoneyError("Object is not an instance of Money class")

        if answer >= 0:
            return Money(answer, self.currency)
        else:
            raise self.MoneyError('Amount cannot be negative')

    def __truediv__(self, other):
        if isinstance(other, Money) and self.currency == other.currency and other.amount != 0:
            answer = self.amount / other.amount
        elif isinstance(other, Money) and other.amount != 0:
            answer = self.amount + other.conversion(self.currency)
        else:
            raise self.MoneyError("Object is not an instance of Money class or equal to 0")
        return Money(answer, self.currency)

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        else:
            raise self.MoneyError("Object is not an instance of Money class")

    def __ne__(self, other):
        if isinstance(other, Money):
            return not self == other
        else:
            raise self.MoneyError("Object is not an instance of Money class")

    def __lt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount < other.amount
        elif isinstance(other, Money):
            return self.amount < other.conversion(self.currency)
        else:
            raise self.MoneyError("Object is not an instance of Money class")

    def __gt__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount > other.amount
        elif isinstance(other, Money):
            return self.amount > other.conversion(self.currency)
        else:
            raise self.MoneyError("Object is not an instance of Money class")

    def __le__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount <= other.amount
        elif isinstance(other, Money):
            return self.amount <= other.conversion(self.currency)
        else:
            raise self.MoneyError("Object is not an instance of Money class")

    def __ge__(self, other):
        if isinstance(other, Money) and self.currency == other.currency:
            return self.amount >= other.amount
        elif isinstance(other, Money):
            return self.amount >= other.conversion(self.currency)
        else:
            raise self.MoneyError("Object is not an instance of Money class")


# Testing Money Class
m = Money(10, 'EUR')
print(m)
m.amount = 15
m.currency = 'AMD'
print(m)
m1 = Money(2000, 'RUB')
m2 = m + m1
m3 = m / m1
m4 = m1 - m
print(m2)
print(m3)
print(m4)
print(m1 == m2)
print(m < m2)
