import os
import time
def clear():
    command = 'cls'
    os.system(command)
clear()
saus = ''
while saus != 'quit':
    saus = str(input('Guess the word, it starts with a \'q\' and ends with \'uit\': '))
    if saus == 'quit':
        print('Good geradeerd')
        time.sleep(1)                  
    else:
        print('Try again: ')   
    