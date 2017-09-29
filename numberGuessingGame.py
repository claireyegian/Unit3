#Claire Yegian
#9/29/17
#numberGuessingGame.py - asks user to guess number between 1 and 100

from random import randint
rnum = randint(1,100)
gnum = int(input('Guess a number between 1 and 100: '))

if gnum==rnum:
    print('You got in on the first try!')
elif:
    while gnum!=rnum:
        if gnum<rnum:
            print('too low')
        elif gnum>rnum:
            print('too high')