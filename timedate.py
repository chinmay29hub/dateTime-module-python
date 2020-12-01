import datetime


year = int(input("Enter the year : "))

d = datetime.datetime(year, 1, 1)

print("Starting day of the year",year," is ",d.strftime("%A"))


