# decorator that counts the number of times a function has been called.
def count(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


class Date:
    def __init__(self, d, m, y):
        self.__year = y
        self.__month = m
        self.__day = d
        self.count = 0

    class DateError(Exception):
        pass

    def __repr__(self):
        return "{}.{}.{}".format(self.day, self.month, self.year)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y < 0:
            raise self.DateError("Year should be bigger than 0")
        self.__year = y

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        if m < 1 or m > 12:
            raise self.DateError("Invalid Month")
        self.__month = m

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        if d < 1 or d > 31:
            raise self.DateError("Invalid Day")
        self.__day = d

    @count
    def add_day(self, days):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        temp = self.day
        if days >= 0:
            temp += days
        else:
            temp += days
            while temp < 1:
                self.sub_month(1)
                temp += days_in_month[self.month]
        while temp > days_in_month[self.month]:
            if self.month == 2 and self.__is_leap_year():
                if temp > 29:
                    temp -= 29
                    self.add_month(1)
            else:
                temp -= days_in_month[self.month]
                self.add_month(1)
        self.day = temp

    @count
    def add_month(self, months):
        temp = self.month
        if months >= 0:
            temp += months
        else:
            temp += months
            while temp < 1:
                self.sub_year(1)
                temp += 12
        while temp > 12:
            temp -= 12
            self.add_year(1)
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if temp == 2 and self.__is_leap_year():
            if self.day > 29:
                self.day = 29
        elif self.day > days_in_month[self.month]:
            self.day = days_in_month[self.month]
        self.month = temp

    @count
    def add_year(self, years):
        if years >= 0:
            self.year += years
        else:
            self.sub_year(abs(years))

    @count
    def sub_year(self, years):
        if years >= 0:
            self.year -= years
        else:
            self.year -= years
            while self.year < 0:
                self.year -= 1

    @count
    def sub_month(self, months):
        if months >= 0:
            for i in range(months):
                if self.month == 1:
                    self.sub_year(1)
                    self.month = 12
                else:
                    self.month -= 1
        else:
            for i in range(abs(months)):
                if self.month == 12:
                    self.add_year(1)
                    self.month = 1
                else:
                    self.month += 1

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.month == 2 and self.__is_leap_year():
            if self.day > 29:
                self.day = 29
        elif self.day > days_in_month[self.month]:
            self.day = days_in_month[self.month]

    @count
    def sub_day(self, days):
        if days >= 0:
            for i in range(days):
                if self.day == 1:
                    if self.month == 1:
                        self.sub_year(1)
                        self.month = 12
                        self.day = 31
                    else:
                        self.sub_month(1)
                        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                        if self.month == 2 and self.__is_leap_year():
                            self.day = 29
                        else:
                            self.day = days_in_month[self.month]
                else:
                    self.day -= 1
        else:
            for i in range(abs(days)):
                if self.day == 31:
                    if self.month == 12:
                        self.add_year(1)
                        self.month = 1
                        self.day = 1
                    else:
                        self.add_month(1)
                        self.day = 1
                else:
                    self.day += 1

    def __is_leap_year(self):
        if self.__year % 4 == 0:
            if self.__year % 100 == 0:
                if self.__year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def __add__(self, other):
        if isinstance(other, Date):
            new_date = Date(self.day, self.month, self.year)
            days = other.day + other.month * 30 + other.year * 365
            new_date.add_day(days)
            return new_date

    def __sub__(self, other):
        if isinstance(other, Date):
            new_date = Date(self.day, self.month, self.year)
            days = other.day + other.month * 30 + other.year * 365
            new_date.sub_day(days)
            return new_date


class Time:
    def __init__(self, h, m, s):
        self.__hour = h
        self.__minute = m
        self.__second = s

    def __repr__(self):
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)

    class TimeError(Exception):
        pass

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, h):
        if h < 0 or h >= 24:
            raise self.TimeError("Invalid Hour")
        self.__hour = h

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, m):
        if m < 0 or m >= 60:
            raise self.TimeError("Invalid minute")
        self.__minute = m

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, s):
        if s < 0 or s >= 60:
            raise self.TimeError("Invalid second")
        self.__second = s

    @count
    def add_second(self, seconds):
        temp = self.second
        if seconds >= 0:
            temp += seconds
        else:
            temp += seconds
            while temp < 0:
                self.sub_minute(1)
                temp += 60
        while temp >= 60:
            temp -= 60
            self.add_minute(1)
        self.second = temp

    @count
    def add_minute(self, minutes):
        temp = self.minute
        if minutes >= 0:
            temp += minutes
        else:
            temp += minutes
            while temp < 0:
                self.sub_hour(1)
                temp += 60
        while temp >= 60:
            temp -= 60
            self.add_hour(1)
        self.minute = temp

    @count
    def add_hour(self, hours):
        temp = self.hour
        if hours >= 0:
            temp += hours
        else:
            temp += hours
            while temp < 0:
                temp += 24
        while temp >= 24:
            temp -= 24
        self.hour = temp

    @count
    def sub_hour(self, hours):
        self.hour -= hours

    @count
    def sub_minute(self, minutes):
        temp = self.minute
        temp -= minutes
        while temp < 0:
            temp += 60
            self.sub_hour(1)
        self.minute = temp

    @count
    def sub_second(self, seconds):
        temp = self.second
        temp -= seconds
        while temp < 0:
            temp += 60
            self.sub_minute(1)
        self.second = temp

    @count
    def sum(self, time):
        self.add_hour(time.__hour)
        self.add_minute(time.__minute)
        self.add_second(time.__second)

    @count
    def __add__(self, other):
        if isinstance(other, Time):
            self.sum(other)
            return self

    @count
    def __sub__(self, other):
        if isinstance(other, Time):
            seconds = other.second + other.minute * 60 + other.hour * 3600
            new_time = Time(self.hour, self.minute, self.second)
            new_time.sub_second(seconds)
            return new_time


class DateTime:
    def __init__(self, d, t):
        self.__date = d
        self.__time = t

    def __repr__(self):
        return "{} {}".format(self.__date, self.__time)

    class DateTimeError(Exception):
        pass

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, d):
        self.__date = d

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, t):
        self.time = t

    @count
    def add_year(self, y):
        self.date.add_year(y)

    @count
    def add_month(self, m):
        self.date.add_month(m)

    @count
    def add_day(self, d):
        self.date.add_day(d)

    @count
    def add_hour(self, h):
        if h < 0:
            raise self.DateTimeError("Invalid Hour")
        days = h // 24
        self.add_day(days)
        self.time.add_hour(h % 24)

    @count
    def add_minute(self, m):
        self.time.add_minute(m)

    @count
    def add_second(self, s):
        self.time.add_second(s)

    @count
    def sub_year(self, y):
        self.date.sub_year(y)

    @count
    def sub_month(self, m):
        self.date.sub_month(m)

    @count
    def sub_day(self, d):
        self.date.sub_day(d)

    @count
    def sub_hour(self, h):
        if h < 0:
            raise self.DateTimeError("Invalid Hour")
        days = h // 24
        self.sub_day(days)
        self.time.sub_hour(h % 24)

    @count
    def sub_minute(self, m):
        self.time.sub_minute(m)

    @count
    def sub_second(self, s):
        self.time.sub_second(s)

    def __add__(self, other):
        if not isinstance(other, DateTime):
            raise self.DateTimeError("Invalid object type")
        new_time = self.time + other.time
        new_date = self.date + other.date
        return DateTime(new_date, new_time)

    def __sub__(self, other):
        if not isinstance(other, DateTime):
            raise self.DateTimeError("Invalid object type")
        new_time = self.time - other.time
        new_date = self.date - other.date
        return DateTime(new_date, new_time)


# Testing Date Class
d = Date(31, 1, 2000)
d.add_month(1)
print(d)
d.add_month(1)
d.add_month(1)
d.add_month(1)
print("Number of add_month function calls {}".format(d.add_month.count))
print(d)
d.sub_month(1)
print(d)
d.year = 2000
d.month = 12
d.day = 31
print(d)
d.add_day(1)
print(d)
d.add_year(1)
print(d)
d2 = Date(1, 1, 2000)
d3 = d + d2
d4 = d - d2
print(d3)
print(d4)

print('\n----------- Testing Time class ----------\n')
# Testing Time class
t = Time(1, 1, 1)
print(t)
t.hour = 12
t.minute = 59
t.second = 59
print(t)
t.add_second(1)
print(t)
t.add_minute(1)
print(t)
t.add_hour(1)
print(t)
t2 = Time(1, 1, 1)
t3 = t + t2
t4 = t - t2
print(t3)
print(t4)

print("\n---------- Testing DateTime class -----------\n")

dt = DateTime(d, t)
print(dt)
dt.add_year(1)
print(dt)
dt.add_month(1)
print(dt)
dt.add_day(1)
print(dt)
dt.add_hour(1)
print(dt)
dt.add_minute(1)
print(dt)
dt.add_second(1)
print(dt)
dt.sub_year(1)
print(dt)
dt.sub_month(1)
print(dt)
dt.sub_day(1)
print(dt)
dt.sub_hour(1)
print(dt)
dt.sub_minute(1)
print(dt)
dt.sub_second(1)
print(dt)
dt2 = DateTime(d3, t3)
dt3 = dt + dt2
print(dt3)
