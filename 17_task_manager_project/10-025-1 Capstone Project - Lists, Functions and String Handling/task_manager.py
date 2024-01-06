# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

#=====constants=======
DATETIME_STRING_FORMAT = "%Y-%m-%d"
today = datetime.now().date()


def register_user():                                    
    username_exists = True                              # Initialise bool so it initaites while loop.
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    while username_exists:                              
        new_username = input("New Username: ")          
        username_exists = False                         # Set username_exists to false to initially assume the username is unique.

        for user in username_password:                  # Loop through username_password dict, easier than looping through file directly.
                             
            if new_username in username_password:       
                print("Username already exist, please use another username.")
                username_exists = True                  # If user name exists, change username_exists to True and stay in while loop.
                break                                   # Don't need to carry on with loop if user already exists, so break out.

    new_password = input("New Password: ")

    confirm_password = input("Confirm Password: ")

    
    if new_password == confirm_password:                # If passwords match, add them to the user.txt file.
        print("New user added")
        username_password[new_username] = new_password
        with open("user.txt", "w") as out_file:         
            user_data = []

            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")            
            out_file.write("\n".join(user_data))

    else:
        print("Passwords do no match")


def write_task(task_list):                  
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []

        for t in task_list:                                # for each task create a list of task details.
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No",
                t['task_number']                           # Added task number to the end.
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))     # Write to file. 


def add_task(username_password, task_list):
    '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return                                               

    # Get task details
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")

    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")
 
    task_number = str(len(task_list) + 1)                   # Add a unique task number to each task.                     

    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False,
        "task_number": task_number                           # Added task number value.
    }

    task_list.append(new_task)

    write_task(task_list)
    print("Task successfully added.")


def view_all(task_list):
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''
    for t in task_list:
        disp_str = f"Task Number:  \t {t['task_number']}\n"
        disp_str += f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Completed: \t {'Yes' if t['completed'] else 'No'}\n"
        disp_str += f"Task Description: \n {t['description']}"
        print("---------------------------------")
        print(disp_str)
        print("---------------------------------")


def view_mine(task_list):
    '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''

    for t in task_list:
        if t['username'] == curr_user:
            disp_str = f"Task Number: \t {t['task_number']}\n"      # Display task number.
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Completed: \t {'Yes' if t['completed'] else 'No'}\n"
            disp_str += f"Task Description: \n {t['description']}"
            print("---------------------------------")
            print(f"\n{disp_str}")
            print("---------------------------------")


def edit_task():
    task_select = input("Input Task Number to find specific task, or press '-1' to go back to the main menu: ")

    if task_select == '-1':
        return
    else:
        # Find the task the user want to edit. 
        found_task = None
        for task in task_list:
            if task['task_number'] == task_select:
                found_task = task
                break

        if found_task:
            print("Task found!")
            print("---------------------------------")
            print(f"{display_task(found_task)}")           # Display task the user wants to edit.
            print("---------------------------------")
            edit = input("Would you like to edit this task? (yes/no): ")
            if edit.lower() == 'yes' and found_task['completed'] == False: 
                detail = input(''' Select one of the following task details to edit:
    1 - Title
    2 - Description
    3 - Who the task is assigned to
    4 - Due date
    5 - Completion
    : ''')
                # Get new detail.
                if detail == '1':
                    found_task['title'] = input("Enter new title: ")
                elif detail == '2':
                    found_task['description'] = input("Enter new description: ")
                elif detail == '3':
                    found_task['username'] = input("Enter who the task is assigned to: ")
                elif detail == '4':
                    while True:
                        try:
                            new_due_date = input('Enter new due date (YYYY-MM-DD): ')
                            found_task['due_date'] = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                            break
                        except ValueError:
                            print("Invalid datetime format. Please use the format specified.")
                elif detail == '5':
                    found_task['completed'] = input('Is the task completed? (yes/no): ').lower() == 'yes'
                
                # Update tasks.txt with the edited task
                write_task(task_list)
                print("Task successfully edited.")

            elif edit.lower() == 'yes' and found_task['completed'] == True:
                print("Task is completed and cannot be edited.")
            else:
                print("Task editing canceled.")
        else:
            print("Task number not found.")


# Added display task functionality so the user can see the selected task they want to edit
def display_task(task): 
    disp_str = f"Task Number: \t {task['task_number']}\n"
    disp_str += f"Task: \t\t {task['title']}\n"
    disp_str += f"Assigned to: \t {task['username']}\n"
    disp_str += f"Date Assigned: \t {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Due Date: \t {task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
    disp_str += f"Completed: \t {'Yes' if task['completed'] else 'No'}\n"
    disp_str += f"Task Description: \n {task['description']}"
    return disp_str


def task_overview():
    '''This function will produce a .txt file which will display
        statistics about how many tasks there are. '''

    # Initialise counter variables.
    num_incompleted = 0
    num_completed = 0
    num_overdue = 0
    num_tasks = 0

    # Loop through tasks if task matches the conditionad 1 to the task counter.
    for t in task_list:
        num_tasks += 1
        if t['completed'] == True:
            num_completed += 1
        elif t['completed'] == False and t['due_date'].date() < today:
            num_overdue += 1
            num_incompleted += 1
        else:
            num_incompleted += 1

    # Calculate percentages
    percentage_incomplete = (num_incompleted/num_tasks)*100
    percentage_overdue = (num_overdue/num_tasks)*100

    # Create string with the statistics
    task_overview_string = f'''Total number of tasks: \t\t\t{num_tasks}
Number of completed tasks: \t\t{num_completed}
Number of incomplete tasks: \t{num_incompleted}
Number of overdue tasks: \t\t{num_overdue}
Percentage of incomplete tasks: {round(percentage_incomplete,2)}%
Percentage of overdue tasks: \t{round(percentage_overdue,2)}% '''

    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(task_overview_string)

    return num_tasks                                         # Return num_tasks to main to be used in user_overview.


def user_overview(num_tasks): 
    '''Function to display statistics about each user and their number of tasks''' 

    num_assigned = 0
    num_assigned_incomplete = 0
    assigned_overdue_incomplete = 0

    # Get number of users and write that and num_tasks to user_overview.txt
    total_users = len(user_data)
    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(f"Total number of users: {total_users}\nTotal mumber of tasks: {num_tasks}")

    for user in username_password.keys():
        
        # For each task if condition is met, add 1 to counter.
        for t in task_list:
            if t['username'] == user and t['completed'] == False and t['due_date'].date() < today:
                num_assigned += 1
                num_assigned_incomplete += 1
                assigned_overdue_incomplete += 1
            elif t['username'] == user and t['completed'] == False:
                num_assigned += 1
                num_assigned_incomplete += 1
            elif t['username'] == user:
                num_assigned += 1
        
        # Calculate percentages
        try:
            percentage_assigned = (num_assigned/num_tasks)*100
            percentage_assigned_completed = ((num_assigned - num_assigned_incomplete)/num_assigned)*100
            percentage_assigned_incomplete = (num_assigned_incomplete/num_assigned)*100
            percentage_overdue_incomplete = (assigned_overdue_incomplete/num_assigned)*100

        except ZeroDivisionError:
            print(f"No tasks assigned to {user}")

            percentage_assigned = 0                         # if no task are assigned to user, set effected values to 0.
            percentage_assigned_completed = 0
            percentage_assigned_incomplete = 0
            percentage_overdue_incomplete = 0

        user_overview_string = f'''\n\nUser: {user}  
Number of assigned tasks: \t\t\t\t{num_assigned}
Percentage of assigned tasks: \t\t\t{round(percentage_assigned,2)}%
Percentage of completed tasks: \t\t\t{round(percentage_assigned_completed,2)}%
Percentage of incomplete tasks: \t\t{round(percentage_assigned_incomplete,2)}%
Percentage of incomplete overdue tasks: {round(percentage_overdue_incomplete,2)}%'''

        with open("user_overview.txt", "a") as user_overview:
            user_overview.write(f"{user_overview_string}")    

        # Reset counter variables to 0
        num_assigned = 0
        num_assigned_incomplete = 0
        assigned_overdue_incomplete = 0


def disp_stats():
    # If admin is logged in they can display stats.
    num_users = 0
    num_tasks = 0

    with open("user.txt", "r") as users:
        for line in users:
            num_users += 1
        
    with open("tasks.txt", "r") as tasks:
        for line in tasks:
            num_tasks += 1

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")   


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:    
        pass

with open("tasks.txt", 'r') as task_file:           
    task_data = task_file.read().split("\n")        # Creates list where each line in tasks.txt is an element.
    task_data = [t for t in task_data if t != ""]   # Removes any empty elements from task data.


task_list = []                                      # Task List is a list where each element is a dictionary which stores task info.
for t_str in task_data:                                  
    curr_t = {}                                     

    
    task_components = t_str.split(";")              # Split each line into separate components of tasks.txt
    curr_t['username'] = task_components[0]         # Associate components to each key in dict.
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False
    curr_t['task_number'] = task_components[6]

    task_list.append(curr_t)                                   # Task list contains a dictionary for each task entry as an element.


# Read user.txt and add the contents to a dictionary.

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")                   # Making a list again which all elements are lines in user.txt.

# Convert to a dictionary
username_password = {} 
for user in user_data:
    username, password = user.split(';')                       # Separate username and password.
    username_password[username] = password                     # Associate password with user name in dict    

#Login User

logged_in = False                               
while not logged_in:                                           # While logged in = false.

    print("LOGIN")                                             # Ask for login.
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():              
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")                     
        continue
    else:
        print("Login Successful!")
        logged_in = True     

while True:
    # Present menu to user.
    print()
    menu = input('''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        register_user()

    elif menu == 'a':
        add_task(username_password, task_list)

    elif menu == 'va':
        view_all(task_list)
        
    elif menu == 'vm':
        view_mine(task_list)
        edit_task()

    elif menu == 'gr':
        num_tasks = task_overview()
        user_overview(num_tasks) 

    elif menu == 'ds' and curr_user == 'admin': 
        disp_stats() 

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")