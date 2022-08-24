#Paint Calculator - Duncan Tasker, Aug 31st 2021

#Import math for the ceiling function
import math
 
#Get user inputs
roomLength = float(input("Enter the room length :: "))
roomWidth = float(input("Enter the room width :: "))
roomHeight = float(input("Enter the room height :: "))
paintCoats = int(input("Enter the number of coats of paint :: "))

#set lists for values, minimum values, and error messages for invalid values
roomDetails = [roomLength, roomWidth, roomHeight, paintCoats]
minValues = [0.0, 3.0, 7.0, 1]
errorMessages = ["Room length", "Room width", "Room height", "Paint coats"] 

#check all values to ensure validity using map to iterate through lists and lambda statement as gerneralised error algorithm
errorCheck = list(map(lambda userInput, minVal, errorMessage: errorMessage if userInput < minVal else "", roomDetails, minValues, errorMessages))

#iterate through the errorCheck list and determine the precesence or type of error
for i in errorCheck:
    if i != "":
        print("\n", i, " is not a valid input", sep="")
        exit()
        
#Calculate room volume by calculating area of each wall and ceiling and subtract door area (7 * 3 = 21) from total area
totalPaint = round(((2 * (roomLength * roomHeight)) + (2 * (roomWidth * roomHeight)) + (roomLength * roomWidth) - 21) * paintCoats, 2)  

#Calculate the number of gallons needed
totalGallons = math.ceil(totalPaint / 400)

#Print output
print("\nYou would need ", totalPaint, " square feet of paint", " or ", totalGallons, " gallon(s)", sep="")