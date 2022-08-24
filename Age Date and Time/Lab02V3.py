#Age Calculator - Duncan Tasker 09/07/2021

import datetime
now = datetime.datetime.now()

currentYear = now.year
currentMonth = now.month
currentDay = now.day

userInput = input("Enter your birthday (mm/dd/yyyy) :: ")

userBirthday = userInput.split("/")
userBirthday = list(map(lambda x: int(x), userBirthday))

if userBirthday[0] > 12 or userBirthday[1] > 31 or userBirthday[2] > currentYear or ((userBirthday[0] > currentMonth and userBirthday[1] > currentDay) and userBirthday[2] > currentYear):
    print("Date entered is invalid")
    exit()

yearAge = now.year - userBirthday[2]

if userBirthday[0] <= currentMonth:
    monthAge = currentMonth - userBirthday[0]
    dayAge = ""
else:
    monthAge = 12 +  currentMonth - userBirthday[0]
    yearAge -= 1
    dayAge = ""
    
if userBirthday[1] <= currentDay:
    dayAge = currentDay - userBirthday[1]
else:
    dayAge = 31 + currentDay - userBirthday[1]
    if monthAge > 0:
        monthAge -= 1
    else:
        yearAge -= 1
    
driveOrVote = ""
if yearAge >= 16:
    driveOrVote = "You are old enough to drive "
if yearAge >= 18:
    driveOrVote += "and you are old enough to vote"

print("you are ", yearAge, " years old, ", monthAge, " months old, and ", dayAge, " days old. ", driveOrVote, sep="")