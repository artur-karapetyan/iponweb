from src.src.HW6.Money import Money
from src.src.HW6.Person import Person


class Doctor(Person):

    def __init__(self, name, surname, gender, age, address, dep, prof, patr, salary):
        super().__init__(name, surname, gender, age, address)
        self.__department = dep
        self.__profession = prof
        self.__patronymic = patr
        self.__salary = salary

    def __repr__(self):
        return '{} {} {} {} {} {} {} {} {}'.format(self.name, self.surname, self.gender,
                                                   self.age, self.address,
                                                   self.__department, self.__profession,
                                                   self.__patronymic, self.__salary)

    class DoctorError(Exception):
        pass

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, department):
        if not isinstance(department, str):
            raise self.DoctorError('Invalid type')
        self.__department = department

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, prof):
        if not isinstance(prof, str):
            raise self.DoctorError('Invalid type')
        self.__profession = prof

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, Money):
            raise self.DoctorError("Invalid type")
        self.__salary = salary


s = Money(500000, 'AMD')
d = Doctor('Artur', 'Karapetyan', 'Male', 20, 'Yerevan', 'Surgery', 'Surgeon', 'Eduard', s)
print(d)
d.department = 'Heart'
print(d)
