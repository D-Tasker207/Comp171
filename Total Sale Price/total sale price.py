#30/08/2021 Class Stuff

#Method to check that all numbers are positive
def errorFinder():
    if itemPrice < 0:
        errorType = "Item price"
    elif saleAmount < 0:
        errorType = "Sale amount"
    elif salesTax < 0:
        errorType = "Sales tax"
    else:
        errorType = ""
    
    return errorType

#Get inputs for variables
itemPrice = int(input("Enter item price :: "))
saleAmount = float(input("Enter sales amount :: "))
salesTax = float(input("Enter sales tax :: "))

#Call method to check for invalid values
error = errorFinder()

#Print Error Message
if error != "":
    print("\n", error, " must not be negative", sep="")
    exit()
    
#Calculate total price
totalPrice = (itemPrice * (1 - (saleAmount / 100))) * (1 + (salesTax / 100))

#Print output
print("\nYou pay: $", round(totalPrice, 2), sep = "")