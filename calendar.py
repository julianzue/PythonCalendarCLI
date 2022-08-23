import time
import datetime

def monthString(num):

    out = ""

    if num == 1:
        out = "January"
    if num == 2:
        out = "Febuary"
    if num == 3:
        out = "March"
    if num == 4:
        out = "April"
    if num == 5:
        out = "May"
    if num == 6:
        out = "June"
    if num == 7:
        out = "July"
    if num == 8:
        out = "August"
    if num == 9:
        out = "September"
    if num == 10:
        out = "October"
    if num == 11:
        out = "November"
    if num == 12:
        out = "December"

    return out

m = int(input("Month (number): "))
y = int(input("Year:  "))

FirstDay = datetime.datetime(y, m, 1)

Month = monthString(FirstDay.month) + " " + str(FirstDay.year)

print(Month)

week = [
    [],
    [],
    [],
    [],
    [],
    []
]

weeknumber = -1

nextDay = FirstDay

round = 0

print("+----+----+----+----+----+----+----+")
print("| Mo | Tu | We | Th | Fr | Sa | Su |")

while True:
    FirstDayName = nextDay.weekday()
    Day = nextDay.day

    if FirstDayName > 0 and round == 0:

        addindex = 0

        while addindex < FirstDayName:
            addindex += 1
            week[weeknumber].insert(addindex, "  ")

    if FirstDayName == 0 and round > 0:
        print("+----+----+----+----+----+----+----+")
        print("| " + " | ".join(week[weeknumber]) + " |")
        weeknumber += 1

    week[weeknumber].insert(FirstDayName, "{:02d}".format(Day))

    nextDay = nextDay + datetime.timedelta(days=1)

    if int(nextDay.month) > int(m):

        addindex = FirstDayName

        while addindex < 6:
            addindex += 1
            week[weeknumber].insert(addindex, "  ")

        print("+----+----+----+----+----+----+----+")
        print("| " + " | ".join(week[weeknumber]) + " |")
        print("+----+----+----+----+----+----+----+")
        break

    round += 1