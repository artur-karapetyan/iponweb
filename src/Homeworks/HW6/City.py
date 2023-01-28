from src.src.HW6.Person import Person


class City:

    def __init__(self, name, mayor, population, language):
        if not isinstance(name, str) or not isinstance(mayor, Person) or not isinstance(population,
                                                                                        int) or not isinstance(language,
                                                                                                               str):
            raise self.CityError('Invalid type')
        self.__name = name
        self.__mayor = mayor
        self.__population = population
        self.__language = language

    def __repr__(self):
        return 'Name {}, Mayor {}, Population {}, Language {}'.format(self.__name, self.__mayor,
                                                                      self.__population, self.__language)

    class CityError(Exception):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise self.CityError('Invalid type')
        self.__name = name

    @property
    def mayor(self):
        return self.__mayor

    @mayor.setter
    def mayor(self, mayor):
        if not isinstance(mayor, Person):
            raise self.CityError('Invalid type')
        self.__mayor = mayor

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population):
        if not isinstance(population, int) or population < 0:
            raise self.CityError('Invalid type')
        self.__population = population

    @property
    def language(self):
        return self.__language


rec = Person('Randall', 'Rhodes', 'Male', 49, 'Yerevan')
mayor = Person('Poghos', 'Poghosyan', 'Male', 50, 'Yerevan')
city = City('Yerevan', mayor, 1000000, 'Armenian')
print(city)
