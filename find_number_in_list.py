# Implement a binary search algorithm to 
# find if a number is in a given sorted list of numbers.
# If true, return the index of the number. 

def find_num(num_list, num):
	if len(num_list) < 1:
		return 'Number not in list.'
	else:
		current_index = (len(num_list)//2)
		if num_list[current_index] == num:
			return current_index
		elif num_list[current_index] >= num:
			return find_num(num_list[0:current_index], num)
		elif num_list[current_index] <= num:
			return current_index + 1 + find_num(num_list[current_index+1:], num)


# Tests: -------------------------------------------------------

A = [0, 1, 4, 7, 8, 10, 14, 17, 19, 21, 22, 25, 30]
B = [0, 2, 3, 5, 9, 11, 12, 18, 19, 20, 23, 25, 30, 34]
C = []
D = [1]

print find_num(A, 0), '(0)'
print find_num(A, 7), '(3)' 
print find_num(A, 21), '(9)'
print find_num(B, 2), '(1)'
print find_num(A, 30), '(12)'  
print find_num(A, 25), '(11)' 
print find_num(B, 30), '(12)'  
print find_num(B, 34), '(13)'  
print find_num(C, 7), '(Nil)'
print find_num(D, 1), '(0)' 
print find_num(D, 0), '(Nil)' 

