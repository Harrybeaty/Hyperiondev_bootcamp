sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
correct_sentence = sentence.replace("!", " ")
print(correct_sentence)

upper_sentence = correct_sentence.upper()
print(upper_sentence)

reverse_sentence = upper_sentence[: :-1]
print(reverse_sentence)

# In the case of this task I could've just re-assigned the sentence variable each time the sentence changed,
# but I figured its better to store the values like I did here, in a real world program, is that correct?