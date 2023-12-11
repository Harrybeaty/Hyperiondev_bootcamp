user_num = 0                                                                      # Initialize variables
input_counter = -1                                                                # Set to -1 so that when the user inputs -1 it isn't used to calculate the average.
total = 0

while user_num != -1:                                                             # While the input isn't -1
    total += user_num                                                             # Adding up the total of the inputs. Goes above the input statement so that when -1 is inputted it isn't included in average. 
    input_counter += 1                                                            # Counting the amount of inputs put in by the user
    user_num = int(input("Enter a number: "))

if input_counter != 0:                                                            # Make sure we're not dividing by 0, in average calculation.
    average = (total)/(input_counter)                                             # Calculate average
    print(f"Average = {average}")                                                 # Print average 
else:
    print("Can't divide by 0, please input other numbers before entering -1")     # If input counter is 0 display message.