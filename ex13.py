from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

cat_name = raw_input("What is the name of your cat? ")
name = raw_input("What is your name? ")

print "Hello %r with a cat called %r!" % (name, cat_name)
