number_of_students =  int(input("How many students are registering for the exam? "))    # Ask user for number of students.

with open('reg_form.txt', 'w') as f:                                                    # Open file in writing mode.

    for student_no in range(number_of_students):                                        # Loop through number of students.

        student_ID = input("Enter student ID number: ")
        if student_no == number_of_students - 1:                                        # Use an if statement to stop an extra line being printed on the last student ID.
            f.write(f"{student_ID} .........")                                          # If last student write student ID without printing new line.
        else:
            f.write(f"{student_ID} ......... \n")                                       # Else print student ID with new line.          
                   