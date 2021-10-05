import time
import os
def clear():
    command = 'cls'
    os.system(command)
clear()
whichDay = input(str('Welke dag van de week? ma, di, wo, do, vr, za, zo: '))
if whichDay == 'ma':
    print('dinsdag, woensdag, donderdag, vrijdag, zaterdag, zondag, maandag')
elif whichDay == 'di':
    print('woensdag, donderdag, vrijdag, zaterdag, zondag, maandag, dinsdag')
elif whichDay == 'wo':
    print('donderdag, vrijdag, zaterdag, zondag, maandag, dinsdag, woensdag')
elif whichDay == 'do':
    print('vrijdag, zaterdag, zondag, maandag, dinsdag, woensdag, donderdag')
elif whichDay == 'vr':
    print('zaterdag, zondag, maandag, dinsdag, woensdag, donderdag, vrijdag')
elif whichDay == 'za':
    print('zondag, maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag')
elif whichDay == 'zo':
    print('maandag, dinsdag, woensdag, donderdag, vrijdag, zaterdag, zondag')
