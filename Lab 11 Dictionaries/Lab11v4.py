#Lab 11 Dictionaries - Duncan Tasker 9/14/2021

#import csv

def readdir():
    directory = []
    tempdict = {}
    file = open("directory-v3-large.csv")
    contents = file.readlines()
    for i in range(1, len(contents)):
        row_contents = contents[i].strip("\n").split(",")
        tempdict["Name"] = row_contents[0]
        tempdict["Location"] = row_contents[1]
        tempdict["Phone Number"] = row_contents[2]
        directory.append(tempdict.copy())
    return directory

def savedir():
    file = open("directory-v3-large.csv", "w")
    file.write('Name,Location,Phone Number\n')
    for i in directory:
        file.write(i['Name']+','+i['Location']+','+i['Phone Number']+'\n')

def searchdir(search_key, search_term):
    #iterate through the array to find item, stores item index for update function, uses search_catagories to change what the user is searching by
    search_categories = ['Name', 'Location', 'Phone Number']
    search_result = []
    search_index = []
    for i in range(len(directory)):
        if directory[i][search_categories[search_key - 1]] == search_term:
            search_result.append(directory[i]['Name'] + ", " + directory[i]['Location'] + ", " + directory[i]['Phone Number'])
            search_index.append(i)
    if search_result == []:
        search_result.append("No entry found in directory")
    return search_result, search_index

def addtodir(name, location, phono):
    #check for duplicate entries, allows for dupliate names, locations, and phone numbers, but not all three in the same entry
    dupe_check = [name + ", " + location + ", " + phono]
    search_dupes = searchdir(1, name)
    for i in search_dupes:
        if dupe_check[0] == i:
            return "\nDuplicate Entry Detected"
        
    add_dict = {'Name' : name, 'Location' : location, 'Phone Number' : phono}
    directory.append(add_dict.copy())
    
    return "\nNew Entry Added"
    
def updateloc(name, newloc, update_key):
    
    update_type = ['Location', 'Phone Number']

    search_entry = searchdir(1, name)
    #see if entries with name exists
    if search_entry[0][0] == "No entry found in directory":
        return "\nCould not find entry, update aborted"
    
    #check to see which of multiple entries a user intended
    elif len(search_entry[0]) > 1:
        print()
        for i in range(len(search_entry[0])):
            print(i + 1, search_entry[0][i])
        user_choice = int(input("Multiple Entries Detected, Please choose number of desired entry :: ")) - 1
        selected_index = search_entry[1][user_choice]
        
    else:
        selected_index = search_entry[1][0]
            
    directory[selected_index][update_type[update_key]] = newloc
    
    return "\nEntry Updated"

def showdir():
    print("\nName,  Location,  Phone Number\n")
    for i in directory:
        print(i['Name'], ",  ", i['Location'], ",  ", i['Phone Number'],sep="")
    
def drawui():
    #the ui method, handles user interface writings and reading inputs
    print("\nSelect Option:\n\t1. Display Directory\n\t2. Search Directory\n\t3. Add a User\n\t4. Update Location or Phone Number\n\t5. Exit Program")
    usr_input = int(input("Enter Number of desiered option :: "))
    if usr_input == 1:
        #Display Directory
        showdir()
    elif usr_input == 2:
        #Search Directory
        print("Would you like to search by:\n\t1. Name\n\t2. Location\n\t3. Phone Number")
        search_key = int(input("Enter number of desiered option :: "))
        search_term = input("Enter term to search :: ")
        search_results = searchdir(search_key, search_term)
        print("")
        for i in search_results[0]:
            print(i)
            
    elif usr_input == 3:
        #Add User
        new_user_name = input("Enter Name for new user :: ")
        new_user_location = input("Enter Location for new user :: ")
        new_user_phono = input("Enter Phone number for new user (use format ###-###-####) :: ")
        print(addtodir(new_user_name, new_user_location, new_user_phono))
        
    elif usr_input == 4:
        #Update Entry
        edit_name = input("Enter Name of entry to be edited :: ")            
        location_or_phono = int(input("Would you like to edit the Location(1) or Phone Number(2) :: "))
        update_val = input("Enter the new Location or Phone Number (use ###-###-#### format) :: ")
        print(updateloc(edit_name, update_val, location_or_phono - 1))
        
    elif usr_input == 5:
        #Save and Exit
        user_save = input("Would you like to save changes? (y/n) :: ")
        if user_save == "y":
            savedir()
            exit()
        elif user_save == "n":
            exit()
    else:
        print("Please input the number (1-5) of the desired action")
    drawui()
    
def main():
    drawui()
         
directory = readdir()
main()