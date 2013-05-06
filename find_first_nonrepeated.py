# Given a string, find the first non repeated character in that string.
# For examle, "total" would return "o"
# "banana" would return b
# "abababc" would return c

user_input = raw_input("Please enter a string.\n")
print "You wrote " + user_input + "." 


first = None

s = user_input.lower().replace(" ","")

for i in range(0,len(s)):
	if (s.count(s[i]) == 1):
		first = s[i]
 		break

if (first != None):
	print "The first letter that doesn't repeat is " + first + "."
else:
	print "All of the letters in this string have at least 2 instances."