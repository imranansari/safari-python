class Date:
    """
    This class represents dates on a human calendar
    """
    def __init__(self, d, m, y):
        Date.month_name_list = ["", "Jan", "Feb"]
        self.day = d
        self.month = m
        self.year = y

    def __str__(self):
        return f"Date: day={self.day}, month={self.month}, year={self.year}"

    def __repr__(self):
        # return self.__str__()
        return str(self)

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def day_of_week(self):
        (m, y) = (self.month, self.year) if self.month >= 3 else (self.month + 12, self.year -1)
        return (self.day + (13 * (m + 1) // 5) + y + y // 4 - y // 100 + y // 400) % 7

# this isn't "static" it's weird :)
    # def bad_funct():
    #     pass

    @staticmethod
    def month_name(month):
        return Date.month_name_list[month]

d = Date(1, 12, 2020)
d1 = Date(3, 12, 2020)
d2 = Date(5, 12, 2020)
print(d)
txt = str(d)
print(txt)

list=[d, d1, d2]
print(list)

d3 = Date(1, 12, 2020)
print(d == d3)

print(f"day of jan 1 2000 is {Date(1, 1, 2000).day_of_week()}")

print(f"Month 1 is {Date.month_name(1)}")
print(f"Month 1 is {d.month_name(1)}")

class Holiday(Date):
    def __init__(self, d, m, y, name):
        super(Holiday, self).__init__(d, m, y)
        self.name = name
    def __str__(self):
        return super(Holiday, self).__str__() + " a holiday called " + self.name

h = Holiday(1, 1, 2020, "new year's day")
print(h)
print(type(h))