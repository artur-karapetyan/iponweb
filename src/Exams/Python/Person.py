class Person:

    def __init__(self, name, surname, gender, age):
        if not isinstance(age, int) or age < 18 or age > 100:
            raise self.PersonError('Invalid type')
        if not isinstance(name, str):
            raise self.PersonError("Invalid type")
        if not isinstance(surname, str):
            raise self.PersonError('Invalid type')
        if gender != 'Male' and gender != 'Female':
            raise self.PersonError('Invalid gender')
        self.__name = name
        self.__surname = surname
        self.__gender = gender
        self.__age = age

    def __repr__(self):
        return "Name: {}, Surname: {}, Gender: {}, Age: {}".format(self.name,
                                                                   self.surname,
                                                                   self.gender,
                                                                   self.age)

    class PersonError(Exception):
        pass

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise self.PersonError("Invalid type")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise self.PersonError('Invalid type')
        self.__surname = surname

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender != 'Male' and gender != 'Female':
            raise self.PersonError('Invalid gender')
        self.__gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int) or age < 18 or age > 100:
            raise self.PersonError('Invalid age')
        self.__age = age

    def __ne__(self, other):
        if self.name != other.name or self.surname != other.surname or self.age != other.age or self.gender != other.gender:
            return False
        return True
