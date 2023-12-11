# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")                                               # SyntaxError because print statement has missing parentheses, fix: add parentheses.
print("\n")                                                                         # SyntaxError because print statement was indented, fix: delete indentation. SyntaxError because print statement has missing parentheses, fix: add parentheses.

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"                                                                      # SyntaxError, age_Str is indented fix: delete indentation. NameError, fix: replace == with =.
#age = int(age_Str)                                                                 # RuntimeError, fix: Remove "years old" from age_str because letters can't become ints.
print("I'm " + age_Str + " years old.")                                             # RuntimeError, print statement was trying concatenate a string with an int, fix Remove age = int(age_Str) and replace age with age_Str. # LogicError, fix: Add spaces to srings so it reads as a sentence.

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = int(age_Str) + int(years_from_now)                                    # RuntimeError, age is not defined, fix: replace with age_Str LogicError: string cannot be added together. fix: convert strings to int.

print("The total number of years: " + str(total_years))                             # SyntaxError print statement missing parentheses, fix: add parentheses. LogicError answer_years is a string and it also should be the variable str(total_years), fix Needed to be converted to a string to print.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12                                                     # SyntaxError because total has not been defined, fix: replace with total_years.
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")    # SyntaxError, fix: add parentheses. SyntaxError because total_months is a int and were concatenating with a string, fix: convert to string.

#HINT, 330 months is the correct answer

# Is a ValueError or TypeError classed as a SyntaxError