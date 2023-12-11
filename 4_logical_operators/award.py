swimming_mins = int(input("Swimming time in minutes: ")) # Unsure whether the task wanted values from the user or if I could just assign them in the script. 
running_mins = int(input("Running time in minutes: "))
cycling_mins = int(input("Cycling time in minutes: "))

total_mins = swimming_mins + running_mins + cycling_mins
print(f"Total time: {total_mins} minutes")

if total_mins <= 100:
    print("Award: Provincial Colours")
elif total_mins <= 105:
    print("Award: Provincial Half Colours")
elif total_mins <= 110:
    print("Award: Provincial Scroll")
else:
    print("No award")
