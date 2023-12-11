# This program takes a special 3 words where they can be put in any order and they will make a sentence. The user inputs numbers 1-3 which decides the order of the sentence.

words = {                                                                       # Initialise dictionary of words.
    1 : "are",
    2 : "there",
    3 : "none" ,
}

order = input("Please enter the numbers 1 ,2 ,3 in any order EG 2, 1, 3: ")     # Get the order from the user.
positions = order.split(", ")                                                   # Split the input into a list of strings containing each number and maintaining the order it was inputted.
 
if (                                                                            # Check statement - Chat GPT did this, I understand what and how its doing this, but wouldn't have thought of this at this point in time.    
    len(positions) == 3                                                         # Check 3 numbers have been inputted.
    and all(pos.isdigit()                                                       # Check 'positions' is all numbers    
            and 1 <= int(pos) <= 3 for pos in positions)                        # Check numbers are between and including 1 and 3.
    and positions[0] != positions[1] != positions[2]                            # Check all the numbers are different
):
    position1, position2, position3 = map(int, positions)                       # Assign elements in positions to their own varibale.

    if position1 == 1:                                                                                  # Add punctuation to make each sentence make sense and print the sentences.
        print(f"{words[position1].capitalize()} {words[position2]} {words[position3]}?")                # Add "?" for questions.
    elif position2 == 2 and position3 == 3:                                                             # This conditional must be second, if it was first you can have an 1, 2, 3 where it would output "Are, there none." rather than "Are there none?"
        print(f"{words[position1].capitalize()}, {words[position2]} {words[position3]}.")               # Add comma after first word for "There, none are" Not sure if this is actually a sentence but for the sake of this programme I'm going to say it is.
    else:
        print(f"{words[position1].capitalize()} {words[position2]} {words[position3]}.")                # Condition when just a "." is needed at the end.

else:
    print("Invalid. Please enter 3 unique numbers between 1 and 3 separated by a comma and a space.")   # Print error when user input is not correct.