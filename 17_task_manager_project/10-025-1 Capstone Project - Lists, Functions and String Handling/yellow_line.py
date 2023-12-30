username_password = {
        'admin': 'password',
        'harry': 'beaty', 
    }
def append_username_password():
    new_entry = {
        'jake': 'fabi', 
    }
    username_password.update(new_entry)

def print_password():
    print(username_password)

append_username_password()
print_password()
