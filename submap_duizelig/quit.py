import os
import time
def clear():
    command = 'cls'
    os.system(command)
clear()
getal = 0 
saus = ''
while saus != 'quit':
    saus = str(input('Guess the word, it starts with a \'q\' and ends with \'uit\': '))
    if saus == 'quit':
        getal = getal + 1 
        print(getal + 'Good geradeerd')
        time.sleep(1)                  
    else:
        print('Try again: ')   
    