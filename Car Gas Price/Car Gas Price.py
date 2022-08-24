#25/08/2021 Duncan Tasker

#user input for car gas usages
newCarMPG = int(input("Enter fuel efficiency of the new car :: "))
oldCarMPG = int(input("Enter fuel efficiency of the old car :: "))

#check that mpg are positive numbers above 0
if newCarMPG <= 0 or oldCarMPG <= 0:
    print("\nCar gas usage cannot be negative or zero")
    exit()
    
#user input for miles travelled
milesTravelled = int(input("Enter amount of miles travelled :: "))

#check miles travelled is positive
if milesTravelled < 0:
    print("\nCannot have negative miles travelled")
    exit()
    
#user input for price of gas
gasPrice = float(input("Enter price of gas per gallon :: "))

#determine gas usage
newCarGas = milesTravelled / newCarMPG
oldCarGas = milesTravelled / oldCarMPG
gasSaved = oldCarGas - newCarGas

#determine the money saved, round to 2 decimal places
moneySaved = gasSaved * gasPrice
moneySaved = round(moneySaved, 2)

#see if user gains or loses money
if moneySaved > 0:
    gainOrLoss = "save"
else:
    gainOrLoss = "lose"

#print output
print("\nYou ", gainOrLoss, ": $", abs(moneySaved),sep="")

