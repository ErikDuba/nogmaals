import time
import os
def clear():
    command = 'cls'
    os.system(command)
clear()
launch = str(input('Do you want to launch \'Het raketje\'? yes/no: '))
if launch == 'yes':
    i = 30
    while i > -1:
        clear()
        print(i)
        i = i - 1
        time.sleep(1)
    print('\'Het raketje\' is on it\'s million mile journey to Saturn! ')
elif launch == 'no':
    print('The rocket exploded and 721 people died...')
