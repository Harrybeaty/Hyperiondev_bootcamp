### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    def __init__(self, email_address, subject_line, email_content):
    # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list.
    order_confirmation = Email("mail@urbanindustries.co.uk", "Thanks for your order", "Thanks for your order, your booking number is 123.")
    order_dispatched = Email("mail@urbanindustries.co.uk", "Order is on its way", "Your order will be with you in 2 days")
    order_tracked = Email("mail@royalmail.co.uk", "Here's your tracking number", "Tracking number: 1234, your order is with the courier and will arrive at 10:00 am.")
    inbox.extend([order_confirmation, order_dispatched, order_tracked])

def list_emails():
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    print("\nInbox")
    for email_number, email in enumerate(inbox, start=1):               # Enumerate loops through the list but associates an index with each value/element.
        print(email_number, email.subject_line)

def read_email(index):
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    print(f"\nEmail number {index}")
    print(f'''Email from: {inbox[index].email_address}
Subject: {inbox[index].subject_line}
Email Content: {inbox[index].email_content}''')
    inbox[index].has_been_read = True

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.
menu = True

while menu:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        while True:
            list_emails()
            index = input("\nPlease input the email number of the email you would like to read? ")
            try:
                index = int(index)
                if 1 <= index <= len(inbox):
                    break
                else:
                    print("Invalid email number. Please try again")
            except ValueError:
                print("Invalid email number. Please try again")
        read_email(index)
    elif user_choice == 2:
        # add logic here to view unread emails
        print("\nUnread Emails")
        for email in inbox:
            if email.has_been_read == False:
                print(f"Subject: {email.subject_line}")

    elif user_choice == 3:
        # add logic here to quit appplication
        print("\nGoodbye!!\n")
        menu = False
        
    else:
        print("Oops - incorrect input.")

