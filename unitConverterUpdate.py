#Claire Yegian
#9/29/17
#unitConverterUpdate.py - converts units // update: on loop, quit option, error message

while True:
    num = int(input('Enter number 1 for kilometers to miles, 2 for kilograms to pounds, 3 for liters to gallons, 4 for Celsius to Fahrenheit, and 5 to quit: '))
    if num==1:
        km = float(input('Enter the kilometers: '))
        miles = km*0.621371
        print('This is equal to', miles, 'miles')
    elif num==2:
        kg = float(input('Enter the kilograms: '))
        pounds = kg*2.20462
        print('This is equal to', pounds, 'pounds')
    elif num==3:
        liters = float(input('Enter the liters: '))
        gallons = liters*0.264172
        print('This is equal to', gallons, 'gallons')
    elif num==4:
        cel = float(input('Enter the degrees in Celsius: '))
        fahr = cel*1.8+32
        print('This is equal to', fahr, 'degrees Fahrenheit')
    elif num==5:
        break
