#Claire Yegian
#9/29/17
#perfectNumber.py - finds if number is perfect

num = int(input('Enter a number: '))
i = 1
total = 0
while i<num:
    if num%i == 0:
        div = i
        total = total + div
    i = i + 1