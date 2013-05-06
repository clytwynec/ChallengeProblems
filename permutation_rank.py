# Problem of the Day #2:
# Given a string, find its index in the alphabetically sorted list of all of the 
# permutations of that word.
# For example, given the string "hat", the alphabetically sorted array of 
# permutations is: [ "aht", "ath", "hat", "hta", "tah", "tha" ]
# So, "hat" is the 3rd word in that array (index 2).


# Get User Input 
user_input = raw_input("Please enter a string.\n")
formatted_input = user_input.lower().replace(" ", "")


# Function to get list of permutations
def find_permutations(string):
	#base case
    if len(string) < 1:
        return [string]

    #recursive case    
    else:
        permutations = []
        for i in range(0, len(string)):
            sub_string = string[0:i] + string[i+1:]
            for j in find_permutations(sub_string):
                permutations.append(string[i:i+1] + j)
        return permutations


# Call to function and sort list alphabetically
permutations = find_permutations(formatted_input)
permutations.sort()

# Find the Index of user input and print the answer
index_of_input = permutations.index(formatted_input)
print index_of_input

