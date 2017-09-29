#Claire Yegian
#9/29/17
#divisors.py - finds all divisors of a number

num = int(input('Enter a number: '))
while i<num:
    if num%i == 0:
        div = i
        print(div)
    i = i+1
