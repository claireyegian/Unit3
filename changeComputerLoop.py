#Claire Yegian
#10/12/17
#changeComputerLoop.py - outputs change in given number

num = int(input('Enter the number of cents you need to give in change: '))

quarters = 0
While num>=25:
    num = num - 25
    quarters = quarters + 1

dimes = 0
While num>=10:
    num = num - 10
    dimes = dimes + 1

nickels = 0
While num>=5:
    num = num - 5
    nickels = nickels + 1

pennies = 0
While num>=1:
    num = num - 1
    pennies = pennies + 1

print('You have', quarters, 'quarters, ', dimes 'dimes, ', nickels, 'nickels, and ', pennies, 'pennies')
