from sys import argv

script, user_name, catName = argv
user_input = '> ' 

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(user_input)

print "Where do you live %s?" % user_name
lives = raw_input(user_input)

print "Who is %s?" % catName
friend = raw_input(user_input)

print "What type of computer do you have?"
computer = raw_input(user_input)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
%r is your %r. He sounds really cool!
And you have a %r computer. Nice!
""" % (likes, lives, catName, friend, computer)