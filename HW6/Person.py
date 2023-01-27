from src.src.HW6.Money import Money


class Company:

    def __init__(self, n, f, e):
        if not isinstance(n, str) or not isinstance(f, int) or not isinstance(e, int):
            raise self.CompanyError('Invalid type')
        self.__company_name = n
        self.__founded_at = f
        self.__employees_count = e

    def __repr__(self):
        return "Company name: {}, Founded at: {}, Number of employees: {}".format(self.company_name, self.founded_at,
                                                                                  self.employees_count)

    class CompanyError(Exception):
        pass

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, n):
        if not isinstance(n, str):
            raise self.CompanyError('The name should be string')
        self.__company_name = n

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, f):
        if not isinstance(f, int):
            raise self.CompanyError('Date should be an integer')
        self.__founded_at = f

    @property
    def employees_count(self):
        return self.__employees_count

    @employees_count.setter
    def employees_count(self, e):
        if not isinstance(e, int) or e < 0:
            raise self.CompanyError('Count should be an integer')
        self.__employees_count = e


class Job:
    def __init__(self, c, s, e, p):
        if not isinstance(c, Company) or not isinstance(s, Money) or not isinstance(e, int) or not isinstance(p, str):
            raise self.JobError('Invalid type')
        self.__company = c
        self.__salary = s
        self.__experience_year = e
        self.__position = p

    def __repr__(self):
        return "Company: {}, Salary: {}, Experience: {}, Position: {}".format(self.company, self.salary,
                                                                              self.experience_year, self.position)

    class JobError(Exception):
        pass

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, c):
        if not isinstance(c, Company):
            raise self.JobError('Invalid type of company')
        self.__company = c

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        if not isinstance(s, Money) or s < 0:
            raise self.JobError('Invalid type of salary')
        self.__salary = s

    @property
    def experience_year(self):
        return self.__experience_year

    @experience_year.setter
    def experience_year(self, e):
        if not isinstance(e, int) or e < 0:
            raise self.JobError('Years of experience should be an integer')
        self.__experience_year = e

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, p):
        if not isinstance(p, str):
            raise self.JobError('Position should be a string')
        self.__position = p


class Person:

    def __init__(self, n, s, g, ag, ad):
        self.__name = n
        self.__surname = s
        self.__gender = g
        self.__age = ag
        self.__address = ad
        self.__friends = []
        self.__job = []

    def __repr__(self):
        return "Name: {}, Surname: {}, Gender: {}, Age: {}, Address: {}, Friends: {}, Job: {}".format(self.name,
                                                                                                      self.surname,
                                                                                                      self.gender,
                                                                                                      self.age,
                                                                                                      self.address,
                                                                                                      self.__friends,
                                                                                                      self.__job)

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
        if gender != 'Male' or gender != 'Female':
            raise self.PersonError('Invalid gender')
        self.__gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int) or age < 0:
            raise self.PersonError('Invalid type')
        self.__age = age

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not isinstance(address, str):
            raise self.PersonError('Invalid type')
        self.__address = address

    def add_friend(self, f):
        if not isinstance(f, Person):
            raise self.PersonError('Invalid type')
        self.__friends.append(f)

    def remove_friend(self, f):
        self.__friends.remove(f)

    def add_job(self, j):
        if not isinstance(j, Job):
            raise self.PersonError('Invalid type')
        self.__job.append(j)
        j.company.employees_count = j.company.employees_count + 1

    def remove_job(self, j):
        if not isinstance(j, Job):
            raise self.PersonError('Invalid type')
        self.__job.remove(j)
        j.company.employees_count = j.company.employees_count - 1

    def display_job(self):
        for j in self.__job:
            print(j)


c = Company("Valod's company", 2002, 444)
print(c)
s = Money(140000, 'USD')
j = Job(c, s, 10, "Havaqarar")
print(j)
p = Person("Valod", "Poghosyan", "Male", 40, "Yerevan")
print(p)
friend = Person('Poghos', 'Poghosyan', "Male", 39, "Yerevan")
p.add_job(j)
p.add_friend(friend)
p.display_job()
print(c)
p.remove_job(j)
p.display_job()
