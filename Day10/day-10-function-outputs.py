###################################
#
# 100 Days of code bootcamp 2021
# (Udemy course by Angela Yu)
# 
# Day 10 exercises - Christopher Hagan
#
###################################

# From day 3 exercise

def isLeapYear(year):
    """Whether or not a specified year is a leap year"""
    if (year % 4 == 0):
        if (year % 100 == 0 and year % 400 != 0):
            leap_year = False
        else:
            leap_year = True    
    else:
        leap_year = False

    return leap_year


def daysInMonth(year, month):
    """Specify the year and month as integers
    return the numbers of days in that month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and isLeapYear(year):
        return 29
    else:
        return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = daysInMonth(year, month)
print(days)
