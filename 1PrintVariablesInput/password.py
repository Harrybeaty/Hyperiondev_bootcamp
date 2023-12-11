password = input("Password: ")
attempted_password = input("What is the password: ")
incorrect_password_list = []

if attempted_password == password:
    print(f"{password}")

else:
    while attempted_password != password:
        incorrect_password_list.append(attempted_password)         # Append adds attempted passoword to the end of the list.
        attempted_password = input("What is the password: ")
        
    print(f"Correct password: {password}")
    print(f"Incorrect passwords: {', '.join(incorrect_password_list)}") # Join, joins the elements in a list with specified characters in between.