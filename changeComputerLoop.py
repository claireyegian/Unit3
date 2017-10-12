#Claire Yegian
#10/12/17
#changeComputerLoop.py - outputs change in given number

num = int(input('Enter the number of cents you need to give in change: '))

quarters = 0
while num>=25:
    num = num - 25
    quarters = quarters + 1
print('Quarters: ', quarters)

dimes = 0
while num>=10:
    num = num - 10
    dimes = dimes + 1
print('Dimes: ', dimes)

nickels = 0
while num>=5:
    num = num - 5
    nickels = nickels + 1
print('Nickels: ', nickels)

pennies = 0
while num>=1:
    num = num - 1
    pennies = pennies + 1
print('Pennies: ', pennies)