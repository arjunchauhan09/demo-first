year = 2011

if (year % 400 == 0) or  (year % 4 == 0 and year % 100 != 0):
    print(year,"year is leAP YEAR ")
else:
    print(year, "is not leap year")