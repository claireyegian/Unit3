#Claire Yegian
#10/3/17
#fri13.py - finds next 10 friday the 13ths

from calendar import weekday
from datetime import date

day2 = int(date.today().day)
month2 = int(date.today().month)
year2 = int(date.today().year)

fri13 = 0
while fri13<=10:
    weekda = weekday(year2,month2,13)
    if weekda==4:
        print(month2,'/13/', year2)
        fri13 += 1
    if month2!=12:
        month2 += 1
    else:
        month2 = 1
        year2 = year2 + 1