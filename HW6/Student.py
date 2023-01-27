from src.src.HW6.City import City
from src.src.HW6.DateTime import Date
from src.src.HW6.Person import Person
from src.src.HW6.University import University


class Student(Person):

    def __init__(self, name, surname, gender, age, address, university, faculty, course, started_at):
        super().__init__(name, surname, gender, age, address)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__started_at = started_at

    def __repr__(self):
        return '{} {} {} {} {}, {}, Faculty: {}, Course: {}, Started: {}'.format(self.name,
                                                                                 self.surname,
                                                                                 self.gender,
                                                                                 self.age,
                                                                                 self.address,
                                                                                 self.__university,
                                                                                 self.__faculty,
                                                                                 self.__course,
                                                                                 self.__started_at)

    class StudentError(Exception):
        pass

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, university):
        if not isinstance(university, University):
            raise self.StudentError('Invalid type')
        self.__university = university

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        if not isinstance(faculty, str):
            raise self.StudentError('Invalid type')
        self.__faculty = faculty

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        if not isinstance(course, int) or course < 0:
            raise self.StudentError('Invalid type')
        self.__course = course

    @property
    def started_at(self):
        return self.__started_at


rec = Person('Randall', 'Rhodes', 'Male', 49, 'Yerevan')
mayor = Person('Poghos', 'Poghosyan', 'Male', 50, 'Yerevan')
city = City('Yerevan', mayor, 1000000, 'Armenian')
d = Date(23, 4, 1991)
uni = University('AUA', d, rec, city)
date = Date(26, 8, 2019)
s = Student('Artur', 'Karapetyan', 'Male', 20, 'Yerevan', uni, 'Computer Science', 2, date)
print(s)
s.course = 3
print(s)
