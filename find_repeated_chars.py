from collections import defaultdict
# write function that finds the first repeated character in a string
# Return the character or None

# def find_first_repeated_char(string):
# 	for i in range(len(string)):
# 		for j in range(len(string)):
# 			if i != j and string[i] == string[j]:
# 				return string[i]
# 	else:
# 		return None

# def find_first_repeated_char(string):
# 	for i in range(len(string)):
# 		if string[i] in string[0:i] or string[i] in string[i+1:]:
# 			return string[i]
# 	else:
# 		return None


def find_first_repeated_char(string):
	chars = defaultdict(lambda:0)
	for char in string:
		chars[char] += 1
	for char in string:
		if chars[char] > 1:
			return char

print find_first_repeated_char('abcdc')
print find_first_repeated_char('abbcdc')
print find_first_repeated_char('abcde')
