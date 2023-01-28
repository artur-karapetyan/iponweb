from src.src.HW6.City import City
from src.src.HW6.DateTime import Date
from src.src.HW6.Money import Money
from src.src.HW6.Person import Person
from src.src.HW6.University import University


class Teacher(Person):

    def __init__(self, name, surname, gender, age, address, university, faculty, experience, start_work_at, subject,
                 salary):
        super().__init__(name, surname, gender, age, address)
        self.__university = university
        self.__faculty = faculty
        self.__experience = experience
        self.__start_work_at = start_work_at
        self.__subject = subject
        self.__salary = salary

    def __repr__(self):
        return '{} {} {} {} {}, {}, Faculty: {}, Experience: {}, Started: {}, Subject: {}, Salary: {}'.format(self.name,
                                                                                                              self.surname,
                                                                                                              self.gender,
                                                                                                              self.age,
                                                                                                              self.address,
                                                                                                              self.__university,
                                                                                                              self.__faculty,
                                                                                                              self.__experience,
                                                                                                              self.__start_work_at,
                                                                                                              self.__subject,
                                                                                                              self.__salary)

    class TeacherError(Exception):
        pass

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, experience):
        if not isinstance(experience, int) or experience < 0:
            raise self.TeacherError('Invalid type')

    @property
    def start_work_at(self):
        return self.__start_work_at

    @property
    def subject(self):
        return self.__subject

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        if not isinstance(faculty, str):
            raise self.TeacherError('Invalid type')
        self.__faculty = faculty

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, Money):
            raise self.TeacherError('Invalid type')
        self.__salary = salary


rec = Person('Randall', 'Rhodes', 'Male', 49, 'Yerevan')
mayor = Person('Poghos', 'Poghosyan', 'Male', 50, 'Yerevan')
city = City('Yerevan', mayor, 1000000, 'Armenian')
d = Date(23, 4, 1991)
uni = University('AUA', d, rec, city)
date = Date(26, 8, 2019)
s = Money(500000, 'AMD')
t = Teacher('Artur', 'Karapetyan', 'Male', 20, 'Yerevan', uni, 'Computer Science', 5, date, 'Python', s)
print(t)
