# Problem of the Day #2:
# Given a string, find its index in the alphabetically sorted list of all of the 
# permutations of that word.
# For example, given the string "hat", the alphabetically sorted array of 
# permutations is: [ "aht", "ath", "hat", "hta", "tah", "tha" ]
# So, "hat" is the 3rd word in that array (index 2).

puts "Please enter a string:"
user_input = gets.chomp.downcase.delete(" ").split("")
output = user_input.permutation.to_a.sort.index(user_input)
puts output
