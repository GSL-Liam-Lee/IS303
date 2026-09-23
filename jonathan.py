print("================================")
print("ROAD TRIP PLANNER")
print("================================\n")

user_name = input('What is your name? ')
travel_location = input('Where are you traveling? ')
travel_distance = float(input('How many miles is the trip one way? '))
car_gasmileage = float(input("What is your vehicle's miles per gallon? "))
gas_price = float(input("What is the gas price per gallon? "))
num_travelers = float(input("How many travelers are going? "))
cost = gas_price*2*travel_distance/car_gasmileage


print("================================")
print("TRIP SUMMARY")
print("================================")
print(f"Traveler: {user_name.upper()}")
print(f"Destination: {travel_location.capitalize()}\n")
print(f"Gallons of Gas: ${gas_price}")
print(f"Gas cost: ${cost:.2f}\n")

print(f"Cost per traveler: ${cost/num_travelers:.2f}")
print("================================")
print("Have a good trip!")