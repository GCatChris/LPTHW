# import argv variable for command line arguments
from sys import argv

# 2 command line arguments
script, filename = argv

# txt variable which holds open file
txt = open(filename)

# output the name of the file
print "Here's your file %r: " % filename
# output the contents of the file
print txt.read()
"""
# have user input the name of the file again
print "Type the filename again:"
file_again = raw_input("> ")

# open the file
txt_again = open(file_again)
# output the contents of the file
print txt_again.read()
"""