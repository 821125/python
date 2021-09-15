class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.day, self.month, self.year}"

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 2021


dt1 = Date.from_string('11-09-2012')
dt2 = Date.from_string('12-10-2020')
print(dt1)
print(dt2)
is_date1 = Date.is_date_valid('11-09-2012')
is_date2 = Date.is_date_valid('45-09-2012')
print(is_date1)
print(is_date2)
print(Date.is_date_valid('45-01-2000'))
