# Changing the case of alternate letters
user_string =  input("Please type a sentence or word: ")    # Get string from user.
final_string = ""                                           # Initialise final string to be used later.    

for index in range(len(user_string)):                       # Set a for loop to count the position of each charcter in the user's string.
    if index % 2 == 0:                                      # If the index is even, convert the letter at that index to upper case.
        letter = user_string[index].upper()
    else:                                                   # If the index is odd, then convert the letter in that position to lower case.
        letter = user_string[index].lower()

    final_string += letter                                  # Concatenate each letter in each iteration to make the final string.

print(final_string)                                         # Print the final string. 

# Changing the case of alternate words.
#words_list = []                                            # Initialise words_list for later use.
list_string = user_string.split(" ")                        # Split user_string into a list where each element is a word. 

words_list = [word.upper() if index % 2 == 0 else word.lower() for index, word in enumerate(list_string)]

""" for position in range(len(list_string)):                    # Set a loop to count the position of each element in the list.
    if position % 2 == 0:                                   # If position is even, convert the word in that position to upper case.
        word = list_string[position].upper()
    else:                                                   # If position is odd, convert the word in that position to lower case.
        word = list_string[position].lower()
    
    words_list.append(word)    """                              # For each iteration add each word to the end of words_list.        

alternate_word_string = " ".join(words_list)                # Join each word in words_list by a space.
print(alternate_word_string)                                # Print the final string.