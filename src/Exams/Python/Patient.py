from src.Exams.Python.Person import Person


class Patient(Person):

    def __init__(self, name, surname, gender, age):
        super().__init__(name, surname, gender, age)

    def __repr__(self):
        return super().__repr__()

    def __ne__(self, other):
        return super().__ne__(other)
