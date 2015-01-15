# variable with string manipulation
x = "There are %d types of people." % 10
#string variable
binary = "binary"
#string variable
do_not = "don't"
# variable with string manipulation
y = "Those who know %s and those who %s." % (binary, do_not)

#print variable x
print x
#print variable y
print y

# variable with string manipulation with raw_data
print "I said: %r." % x 
#variable with string manipulation
print "I also said: '%s'." % y

#boolean variable
hilarious = False
#string with boolean variable
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
print w + e
