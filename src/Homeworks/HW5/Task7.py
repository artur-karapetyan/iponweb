class Date:
    def __init__(self, d, m, y):
        self.year = y
        self.month = m
        self.day = d

    def __repr__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)

    def add_day(self, day):
        self.day += day
        while self.day > self.__days_of_month():
            self.day -= self.days_of_month()
            self.add_month(1)

    def add_month(self, months):
        self.month += months
        while self.month > 12:
            self.month -= 12
            self.add_year(1)

    def add_year(self, years):
        self.year += years

    def __days_of_month(self):
        if self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            if self.__is_leap_year():
                return 29
            else:
                return 28
        else:
            return 31

    def __is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def __repr__(self):
        return "{}:{}:{}".format(self.hour, self.minute, self.second)

    def add_second(self, seconds):
        self.second += seconds
        while self.second >= 60:
            self.second -= 60
            self.add_minute(1)

    def add_minute(self, minutes):
        self.minute += minutes
        while self.minute >= 60:
            self.minute -= 60
            self.add_hour(1)

    def add_hour(self, hours):
        self.hour += hours
        while self.hour >= 24:
            self.hour -= 24

    def sum(self, time):
        self.add_hour(time.hour)
        self.add_minute(time.minute)
        self.add_second(time.second)


d = Date(6, 2, 2002)
print(d)
d.add_day(15)
print(d)
d.add_month(2)
print(d)
d.add_year(4)
print(d)

t = Time(12, 2, 14)
print(t)
t.add_hour(4)
print(t)
t.add_minute(98)
print(t)
t.add_second(234)
print(t)

t2 = Time(16, 24, 45)
t.sum(t2)
print(t)
