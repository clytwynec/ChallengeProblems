# Given a string, find the first non repeated character in that string.
# For examle, "total" would return "o"
# "banana" would return b
# "abababc" would return c

puts "Please enter a string."
raw_input = gets.chomp
puts "You wrote #{raw_input}"

first = nil

input = raw_input.downcase.delete(" ")
s = input.split("")

s.each{|letter|
	if s.count(letter) == 1
		first = letter
		break
	end
}

if first != nil
	puts "The first letter that doesn't repeat is \"#{first}\"."
else 
	puts "All of the letters in this string have at least 2 instances."
end