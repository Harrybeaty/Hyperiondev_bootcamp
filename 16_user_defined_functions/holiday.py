# Holiday Calculator

cost_list = []                                  # Initilise list to allow for easy formatting later
format_list = []                                # Initialise list for formatted costs. 
rental_price = 30                       
hotel_price = 50 

# Calculate hotel price 
def hotel_cost(num_nights):             
    hotel_cost = hotel_price * num_nights
    cost_list.append(hotel_cost)                # Add to cost list for formatting.
    return hotel_cost

# Assign the plane cost based on which city the user is goung to.
def plane_cost(city_flight):
    if city_flight == "Dublin":
        plane_cost = 50
    elif city_flight == "Belfast":
        plane_cost = 40
    elif city_flight == "Edinburgh":
        plane_cost = 60
    elif city_flight == "London":
        plane_cost = 70
        
    cost_list.append(plane_cost)                            # Add to list for formatting later.
    return plane_cost

# Calculate total cost of the rental car.
def car_rental(rental_days):
    car_rental = rental_price * rental_days
    cost_list.append(car_rental)                            # Add to list for formatting later.
    return car_rental

# Calculate total cost of holiday.
def holiday_cost():
    holiday_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)   # Calling the other function within the equaion.
    cost_list.append(holiday_cost)                          # Add to list for formatting later.
    return holiday_cost

# Get Holiday Details
city_flight = input("Which city are you flying to, Dublin, Belfast, Edinburgh, or London? ").capitalize()

if city_flight == "Dublin" or city_flight == "Belfast" or city_flight == "Edinburgh" or city_flight == "London": 
    num_nights = int(input("How many nights are you staying there? "))  
    rental_days = int(input("How many days will you rent a car? "))

    holiday_cost()                                              # Call holiday cost function.

    # For loop used to format costs into money format (£20.00)
    for i in range(len(cost_list)):                             
        format_list.append("{:.2f}".format(cost_list[i]))

    # Print costs
    print(f"Hotel Cost = £{format_list[0]}")
    print(f"Flight Cost = £{format_list[1]}")
    print(f"Car Rental Cost = £{format_list[2]}")
    print(f"Total Holiday Cost = £{format_list[3]}")
    
else:
    print("Please make sure you enter one of the following cities, Dublin, Belfast, Edinburgh, or London") # Print statement if user hasn't typed the correct input.