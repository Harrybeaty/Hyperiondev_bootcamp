name_list = []                              # Initialise name_list for later use.
birthdate_list = []                         # Initialise birthdate_list for later use.

with open('DOB.txt', 'r+') as file:         # Open DOB.txt in read and write mode.
    
    for line in file:                       # Loop through lines
        words = line.split(' ')             # Split the line into a list of the words on each line.
        name = ' '.join(words[:2])          # Join the first two elements (person's name) with a space. 
        birthdate = ' '.join(words[2:])     # Join the rest of the elements (person's birthdate) with a space.
        name_list.append(name)              # Add each name to name_list.
        birthdate_list.append(birthdate)    # Add each birthdate birthdate_list.
        print(name)
        print(birthdate)

""" print("Name")                               # Display list title.
for person_name in name_list:               # For each person in name list print their name.
    print(person_name)                      
print('\n')                                 # Print space between displayed lists
print("Birthdate")                          # Display list title
for person_birthdate in birthdate_list:     # For eaxh person in birthdate_list print their birthdate.    
    print(person_birthdate.strip())     """     # Strip white space at the end because it was printing a extra line inbetween each date.
    