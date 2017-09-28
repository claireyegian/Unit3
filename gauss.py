#Claire Yegian
#9/28/17
#gauss.py - adds numbers

"""
i=100
total = 0
while i>=0:
    total = total + i
    i = i-1
print(total)"""

num1 = int(input('Enter the begining of the range: '))
num2 = int(input('Enter the end of the range: '))
i = num2
total = 0
while i>=num1:
    total = total+i
    i = i-1
print(total)
