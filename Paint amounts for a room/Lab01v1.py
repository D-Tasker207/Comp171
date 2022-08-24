#Paint Calculator - Duncan Tasker, Aug 31st 2021

#import math

#Method to check that all numbers are valid inputs
def errorFinder():
    if roomLength < 0:
        errorType = "Room length"
    elif roomWidth < 3:
        errorType = "Room width"
    elif roomHeight < 7:
        errorType = "Room height"
    #elif paintCoats < 1:
    #    errorType = "Paint coats"
    else:
        errorType = ""
    
    return errorType

#Get inputs
roomLength = float(input("Enter the room length :: "))
roomWidth = float(input("Enter the room width :: "))
roomHeight = float(input("Enter the room height :: "))
#paintCoats = int(input("Enter the number of coats of paint :: "))

#Call method to check for invalid inputs
error = errorFinder()

#Print Error Message
if error != "":
    print("\n", error, " is not a valid input", sep="")
    exit()

#Calculate room volume by calculating area of each wall and ceiling and subtract door area (7 * 3 = 21) from total area
totalPaint = round(((2 * (roomLength * roomHeight)) + (2 * (roomWidth * roomHeight)) + (roomLength * roomWidth) - 21), 2) # * paintCoats

#Calculate the number of gallons needed
#totalGallons = math.ceil(totalPaint / 400)

#Print output
print("You would need ", totalPaint, " square feet of paint") #, " or ", totalGallons, " gallon(s)", sep="")