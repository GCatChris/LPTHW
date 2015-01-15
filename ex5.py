my_name = 'Chris P. Khoury'
my_age = 27 #Not a lie
my_height = 75 # inches
my_weight = 182 #lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's tale about %s." % my_name
print "He's %d centimeters tall." % (my_height * 2.54)
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy"
print "That's %d kilograms." % (my_weight * 0.453592)
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d and %d I get %d" % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)