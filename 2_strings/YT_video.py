word = "hello" 

capital_word = word.capitalize()
print(capital_word)

word_two = "====hello there===="
strip_word_2 = word_two.strip("=")
print(strip_word_2)

rep_word = word.replace("l", "1")
print(rep_word)

position = word[0:3]
print(position) # this prints hel because it goes up to but not including position 3.

every_second_letter = word[0: :2] # This means index from 0 to the end of the string but go in steps of two.
print(every_second_letter)

negative_indexing = word[-1]
print(negative_indexing) # this prints o

reverse_word = word[::-1] # this is saying from start to finish but in steps of -1
print(reverse_word)