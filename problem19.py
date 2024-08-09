
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
def solve():
    monthdict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    ly_monthdict = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    leap_year = False
    sundays = 0
    first_sunday = 6

    for year in range(1901, 2001):
        if year % 4 == 0 and year % 100 != 0:
            leap_year = True
        elif year % 100 == 0 and year % 400 == 0:
            leap_year = True
        else:
            leap_year = False

        if leap_year:
            for month in range(1, 13):
                if first_sunday == 1:
                    sundays += 1
                curr_sunday = first_sunday
                while curr_sunday < ly_monthdict[month]:
                    curr_sunday += 7
                first_sunday = curr_sunday - ly_monthdict[month]
        else:
            for month in range(1, 13):
                if first_sunday == 1:  # Moved this block up
                    sundays += 1
                curr_sunday = first_sunday
                while curr_sunday < monthdict[month]:
                    curr_sunday += 7
                first_sunday = curr_sunday - monthdict[month]
    return sundays


#print(sundays, "Sundays occured on the first of the month")


normal = 365
leap = 366

is_leap = True

for i in range(36,525):
    if i % 5


