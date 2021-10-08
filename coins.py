# name of student: Erik Duba
# number of student: 99068765
# purpose of program: Calculate how much change there is left to be paid
# function of program: It calculates how much change there is left to be paid
# structure of program: Asks some inputs and goes to work with those inputs

toPay = int(float(input('Amount to pay: ')) * 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #change = paid - toPay

if change > 0: #if change is more than 0:
  coinValue = 50 #coinValue will be set equal to 50
  
  while change > 0 and coinValue > 0: #if change and coinValue are both bigger than 0:
    nrCoins = change // coinValue #nrCoins will be change divided by coinValue

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')