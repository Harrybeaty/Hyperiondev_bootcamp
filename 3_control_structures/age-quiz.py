age = int(input("What's your age? "))

if age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:                       # This goes after 65 and 100 conditionals so that if the age is 65 which is still over 40 but the program doesn't print the 40 conditional message as it is skipped.
    print("You're over the hill.")    # Could also write elif 40 <= age < 65: and elif 65 <= age <= 100:, these statements would make the order insignificant.
else:
    print("Age is but a number.")