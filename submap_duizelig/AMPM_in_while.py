import time
import os
def clear():
    command = 'cls'
    os.system(command)

clear()
am = 0
while am <= 11:
    am = am + 1
    print(str(am) + 'AM')
    time.sleep(0.5)
    clear()

pm = 0
while pm <= 11:
    pm = pm + 1
    print(str(pm) + 'PM')
    time.sleep(0.5)
    clear()