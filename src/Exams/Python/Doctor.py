import datetime
from src.Exams.Python.Patient import Patient
from src.Exams.Python.Person import Person


class Doctor(Person):

    def __init__(self, name, surname, gender, age):
        super().__init__(name, surname, gender, age)
        self.__schedule = {}

    def __repr__(self):
        return 'Doctor {} {}, Schedule {}'.format(super().name, super().surname, self.__schedule)

    def is_free(self, time):
        if time.time() < datetime.time(10) or time.time() > datetime.time(18):
            return False
        end = time + datetime.timedelta(minutes=30)
        for date_time, patient in self.__schedule.items():
            if time <= date_time < end:
                return False
        return True

    def is_registered(self, patient):
        return patient in self.__schedule.values()

    def register_patient(self, patient, time):
        if self.is_registered(patient):
            return 'Patient {} already registered'.format(patient)
        if not self.is_free(time):
            return 'DateTime {} already taken from {}'.format(time, self.__schedule[time])
        self.__schedule[time] = patient


# Testing Functions
patient = Patient('Artur', 'Karapetyan', 'Male', 21)
print(patient)
doctor = Doctor('Poghos', 'Poghosyan', 'Male', 45)
print(doctor)
time_reserve = datetime.datetime(2023, 2, 6, 12, 30)
print(doctor.is_free(time_reserve))
print(doctor.is_registered(patient))
doctor.register_patient(patient, time_reserve)
print(doctor.is_registered(patient))
print(doctor)
