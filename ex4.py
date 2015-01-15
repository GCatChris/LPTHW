# variable cars
cars = 100
#variable space_in_a_car designates the number of passengers a car can hold
space_in_a_car = 4.0
# variable drivers
drivers = 30
#variable passengers
passengers = 90
# variable cars_not_driven equal to cars - drivers
cars_not_driven = cars - drivers
# variable cars_driven = drivers
cars_driven = drivers
# variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
