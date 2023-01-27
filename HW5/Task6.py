# Finish class work

class Company:

    def __init__(self, n, f, e):
        self.company_name = n
        self.founded_at = f
        self.employees_count = e

    def __repr__(self):
        return "Company name: {}, Founded at: {}, Number of employees: {}".format(self.company_name, self.founded_at,
                                                                                  self.employees_count)


class Job:
    def __init__(self, c, s, e, p):
        self.company = c
        self.salary = s
        self.experience_year = e
        self.position = p

    def __repr__(self):
        return "Company: {}, Salary: {}, Experience: {}, Position: {}".format(self.company, self.salary,
                                                                              self.experience_year, self.position)

    def change_salary(self, s):
        self.salary = s

    def change_experience_year(self, e):
        self.experience_year = e

    def change_position(self, p):
        self.position = p


class Person:

    def __init__(self, n, s, g, ag, ad):
        self.name = n
        self.surname = s
        self.gender = g
        self.age = ag
        self.address = ad
        self.friends = []
        self.job = []

    def __repr__(self):
        return "Name: {}, Surname: {}, Gender: {}, Age: {}, Address: {}, Friends: {}, Job: {}".format(self.name,
                                                                                                      self.surname,
                                                                                                      self.gender,
                                                                                                      self.age,
                                                                                                      self.address,
                                                                                                      self.friends,
                                                                                                      self.job)

    def add_friend(self, f):
        self.friends.append(f)

    def remove_friend(self, f):
        self.friends.remove(f)

    def add_job(self, j):
        self.job.append(j)
        j.company.employees_count += 1

    def remove_job(self, j):
        self.job.remove(j)
        j.company.employees_count -= 1

    def display_job(self):
        for j in self.job:
            print(j)


c = Company("Valod's company", 2002, 444)
print(c)
j = Job(c, 10000, 10, "Havaqarar")
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
