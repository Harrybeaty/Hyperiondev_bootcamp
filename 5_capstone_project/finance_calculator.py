import math

print()
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan")
print()
print()
calculator_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if calculator_type == "investment":

    # Get investment details 
    print("Please enter the following details:")
    deposit = int(input("Deposit: "))
    interest = int(input("Interest rate: "))/100                # Divide percentage by 100 to use in formulas
    years = int(input("Planned number of years of investment: "))
    interest_type = input("Enter either 'simple' or 'compound' depending on your interest type: ").lower()

    # Check if simple or compound
    if interest_type == "simple":

        # Calculate total
        total = deposit * (1 + interest * years)

    elif interest_type == "compound":

        # Calculate total
        total = deposit * math.pow((1 + interest), years)       # math.pow puts everything before the comma to the power of what behind the comma.
    else:
        print("Please enter either 'simple or 'compound' only.")
    
    format_total = "{:.2f}".format(total)                       # Format to display in money form.
    print(f"Total amount: £{format_total}")

elif calculator_type == "bond":

    # Get bond details
    print("Please enter the following details: ")
    house_value = int(input("Present house value: "))
    interest = (int(input("Interest rate: "))/100)/12                   # Divide by 100 then divide by 12 to get the rate per month.
    months = int(input("Planned number of months for repayment: "))

    # Calculate monthly repayment
    repayment = (interest * house_value)/(1 - (1 + interest)**(- months))
    format_repayment = "{:.2f}".format(repayment)
    print(f"Monthly repayment: £{format_repayment}")    # Format to display in money format.

else:
   
   print("Please input either 'investment' or 'bond'")      
