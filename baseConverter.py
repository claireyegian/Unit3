#Claire Yegian
#10/12/17
#baseConverter.py - changes base-10 to any other base between 2 and 16

base10 = int(input('Enter a base-10 number: '))
base = int(input('What base whould you like to convert to? '))

i = 1
while base10<=(base**i):
    digits = i
    i = i + 1

print(digits)