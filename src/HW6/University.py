from src.src.HW6.City import City
from src.src.HW6.DateTime import Date
from src.src.HW6.Person import Person


class University:

    def __init__(self, name, date, rector, city):
        if not isinstance(name, str) or not isinstance(date, Date) or not isinstance(rector, Person) or not isinstance(
                city, City):
            raise self.UniversityError('Invalid type')
        self.__name = name
        self.__founded_at = date
        self.__rector = rector
        self.__city = city

    def __repr__(self):
        return '{}, Founded at {}, Rector {}, Address {}'.format(self.__name, self.__founded_at
                                                                 , self.__rector, self.__city)

    class UniversityError(Exception):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise self.UniversityError('Invalid type')
        self.__name = name

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, date):
        if not isinstance(date, Date):
            raise self.UniversityError('Invalid type')
        self.__founded_at = date

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, rector):
        if not isinstance(rector, Person):
            raise self.UniversityError('Invalid type')
        self.__rector = rector

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if not isinstance(city, City):
            raise self.UniversityError('Invalid type')
        self.__city = city


rec = Person('Randall', 'Rhodes', 'Male', 49, 'Yerevan')
mayor = Person('Poghos', 'Poghosyan', 'Male', 50, 'Yerevan')
city = City('Yerevan', mayor, 1000000, 'Armenian')
d = Date(23, 4, 1991)
uni = University('AUA', d, rec, city)
print(uni)
