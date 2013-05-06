# Problem of the Day #3

# 1) Given a string, write a function that determines whether or not that string is a palindrome.

# 2) Using that function, write a program that finds the longest palindrome in a given string.

# e.g. "abccdccbd" will return "bccdccb"
# "banana" will return "anana"


# Get string to check
input_word = raw_input("Please enter a word:\n").lower().replace(" ", "")

# Part 1:  Function determines if the argument is a palindrome or not. (returns boolean)
def is_palindrome(chunk):
	if len(chunk) <= 1:
		return True
	else:
		if chunk[0] == chunk[-1]:
			return is_palindrome(chunk[1:-1])
		else:
			return False

# Part 2: Function to find the longest palindrome in a word
def find_longest_palindrome(word):
	palindromes = []
	current_parts = [word]

	while len(current_parts[0]) > 1: 
		for part in current_parts:
			if is_palindrome(part):
				palindromes.append(part)

		if len(palindromes) > 0:
			if len(palindromes) > 1:
				return "The longest palindromes are: " + ", and ".join(palindromes)
			else:
				return "The longest palindrome is: " + palindromes[0] 
		else:
			new_parts = []
			new_parts.append(current_parts[0][0:-1])
			for part in current_parts:
				new_parts.append(part[1:])
			current_parts = new_parts

	return "There are no palindromes."



print find_longest_palindrome(input_word)




