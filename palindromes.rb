# Problem of the Day #3

# 1) Given a string, write a function that determines whether or not that string is a palindrome.

# 2) Using that function, write a program that finds the longest palindrome in a given string.

# e.g. "abccdccbd" will return "bccdccb"
# "banana" will return "anana"

puts "Please enter a word:"
input_word = gets.chomp.downcase.delete(" ")


# Part 1:  Function determines if the argument is a palindrom or not. (returns boolean)
def is_palindrome(chunk)
	if chunk.length <= 1
		return true
	else
		if chunk[0] == chunk[-1]
			return is_palindrome(chunk[1...-1])
		else
			return false
		end
	end
end



def find_longest_palindrome(word)
	palindromes = []
	current_parts = [word]

	while current_parts[0].length > 1 do 
		for part in current_parts
			if is_palindrome(part)
				palindromes.push(part)
			end
		end

		if palindromes.length > 0
			if palindromes.length > 1
				return "The longest palindromes are: " + palindromes.join(", and ")
			else
				return "The longest palindrome is: " + palindromes[0] 
			end
		else
			new_parts = []
			new_parts.push(current_parts[0][0...-1])
			for part in current_parts
				new_parts.push(part[1..-1])
			end
			current_parts = new_parts
		end
	end

	return "There are no palindromes."
end

puts find_longest_palindrome(input_word)






