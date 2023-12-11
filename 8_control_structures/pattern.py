for line in range(0, 9):           # Count up the lines
    
    if line == 0 or line == 8:     # if statement says if on correct line print the correct number of "*" to create pattern.
        print("*")
    elif line == 1 or line == 7: 
        print("**")
    elif line == 2 or line == 6:
        print("***")
    elif line == 3 or line == 5:
        print("****")
    else:
        print("*****")

#for i in range(1, 6):             # Second method with two for loops.
#  print("*" * i)
   
#for i in range(4, 0, -1):
#    print("*" * i)