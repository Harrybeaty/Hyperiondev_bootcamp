# This program takes a special 3 words where they can be put in any order and they will make a sentence. The user inputs numbers 1-3 which decides the order of the sentence.

words = {                                                                       # Initialise dictionary of words.
    1 : "are",
    2 : "there",
    4 : "none"                                                                  # RuntimeError, as it fails to run when the programme is run. It occurs beacuse position3 contains the int 3 but key 3 doesn't exist in the dictionary.            
                                                                                # SyntaxError, the dictionary needs a closing "}" for it to be defined as a dictionary. 

order = input("Please enter the numbers 1 ,2 ,3 in any order EG 2, 1, 3: ")     # Get the order from the user.
positions = order.split(", ")                                                   # Split the input into a list of strings containing each number and maintaining the order it was inputted.
 
if (                                                                            # Check statement - Chat GPT did this, I understand what and how its doing this, but wouldn't have thought of this at this point in time.    
    len(positions) == 3                                                         # Check 3 numbers have been inputted.
    and all(pos.isdigit()                                                       # Check 'positions' is all numbers    
            and 1 <= int(pos) <= 3 for pos in positions)                        # Check numbers are between and including 1 and 3.
    and positions[0] != positions[1] != positions[2]                            # Check all the numbers are different
):
    position1, position2, position3 = map(int, positions)                       # Assign elements in positions to their own variable and convert them to integers.

    if position2 == 2 and position3 == 3:                                                               # LogicError, This conditional must be second, if it is first you can have a 1, 2, 3 input where it would output "Are, there none." which doesn't make grammatical sense. Rather it should be "Are there none?". The error occurs because 1, 2, 3 meets the first condition so the if statement will miss the second condition which is the correct condition for that input.
        print(f"{words[position1].capitalize()}, {words[position2]} {words[position3]}.")               # Add comma after first word for "There, none are" Not sure if this is actually a sentence but for the sake of this programme I'm going to say it is.
    elif position1 == 1:                                                                                # Add punctuation to make each sentence make sense and print the sentences.
        print(f"{words[position1].capitalize()} {words[position2]} {words[position3]}?")                # Add "?" for questions.
    else                                                                                                # SyntaxError missing ':' after else statement, this breaks the rules of python for defining the else statement.
        print(f"{words[position1].capitalize()} {words[position2]} {words[position3]}.")                # Condition when just a "." is needed at the end.

else:
    print("Invalid. Please enter 3 unique numbers between 1 and 3 separated by a comma and a space.")   # Print error when user input is not correct.