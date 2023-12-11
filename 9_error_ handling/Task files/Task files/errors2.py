# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"                                                                                 # RunttimeError, Lion is not a defined variable, fix: replace Lion with "Lion".
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"     # LogicError, This line is in the format of an f string but it is missing the f at the front, fix: add a 'f' to the front.
                                                                                                # LogicError, The sentence doesn't make sense. fix: swap positions of number_of_teeth with animal_type in f string.
print(full_spec)                                                                                # SyntaxError, print statement missing parentheses, Fix: add parentheses around string.

