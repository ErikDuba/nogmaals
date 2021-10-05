import time
import os
def clear():
    command = 'cls'
    os.system(command)
clear()
whichDay = int(input('Welke dag van de week is het? 1 t/m 7: '))
while whichDay <= 7:
    if whichDay == 1:
        print('Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag, Maandag')
        whichDay = 8
    elif whichDay == 2:
        print('Woensdag, donderdag, Vrijdag, Zaterdag, Zondag, Maandag, Dinsdag')
        whichDay = 8
    elif whichDay == 3:
        print('Donderdag, Vrijdag, Zaterdag, Zondag, Maandag, Dinsdag, Woensdag')
        whichDay = 8
    elif whichDay == 4:
        print('vrijdag, zaterdag, zondag, Maandag, Dinsdag, Woensdag, donderdag')
        whichDay = 8
    elif whichDay == 5:
        print('zaterdag, zondag, Maandag, Dinsdag, Woensdag, donderdag, vrijdag')
        whichDay = 8
    elif whichDay == 6:
        print('zondag, Maandag, dinsdag, Dinsdag, Woensdag, vrijdag, zaterdag')
        whichDay = 8
    elif whichDay == 7:
        print('Maandag, Dinsdag, Woensdag, donderdag, vrijdag, Zaterdag, Zondag')
        whichDay = 8
