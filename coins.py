# name of student: Erik Duba
# number of student: 99068765
# purpose of program: Calculate how much change there is left to be paid
# function of program: It calculates how much change there is left to be paid
# structure of program: Asks some inputs and goes to work with those inputs

toPay = int(float(input('Amount to pay: ')) * 100) #it ties your input for how much you owe to the variable toPay and multiplies that by 100
paid = int(float(input('Paid amount: ')) * 100) #it ties your input for how much you already paid to the variable paid and multiplies that by 100
change = paid - toPay #change is set equal to the variable paid minus the variable toPay

if change > 0: #if change is more than 0:
  coinValue = 50 #coinValue will be set equal to 50
  
  while change > 0 and coinValue > 0: #if change and coinValue are both bigger than 0:
    nrCoins = change // coinValue #nrCoins will be equal to change divided by coinValue

    if nrCoins > 0: #if nrCoins is bigger than 0:
      print('return maximum ', nrCoins, ' coins of ', coinValue, ' cents!' ) #it will print the maximal amount of 50cent coins
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #it will ask an input and tie the input to the variable nrCoinsReturned
      change -= nrCoinsReturned * coinValue #it subtracts the right operand from the left operand and assignes the result to the left operand

# comment on code below: each coin value will be assinged a value
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

if change > 0: #if change is bigger than 0 it will print the remaining amount of cents you have left to return
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')