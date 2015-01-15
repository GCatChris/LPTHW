

def number_cruncher(n, i):
	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)
		
		i += 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
i = 0
numbers = []
number_cruncher(6, i)
print "The numbers: "

for num in numbers:
	print num
	