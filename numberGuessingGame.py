#Claire Yegian
#9/29/17
#numberGuessingGame.py - asks user to guess number between 1 and 100

from random import randint
rnum = randint(1,100)

tries = 0
while True:
    gnum = int(input('Guess a number between 1 and 100: '))
    tries = tries + 1
    if gnum<rnum:
        print('too low')
    elif gnum>rnum:
        print('too high')
    elif gnum==rnum:
        break
print('You got it in', tries, 'tries')