from types import *

# write three functions to perform the following operations on a 2 dimensional array:
# 1) flip the array horizontally
# 2) flip the array vertically
# 3) transpose the array
# Examples
# 1) e.g. [1, 2] => [2, 1] or [ [1, 2], [3, 4] ] => [ [2, 1], [ 4, 3] ]
# 2) e.g. [1, 2] => [1, 2] (flipping a 2x1 matrix vertically should keep it the same), [ [1, 2], [3, 4] ] => [ [ 3, 4], [1 , 2] ]
# 3) e.g. [1, 2] => [ [1], [2] ] (2x1 becomes 1x2) or [ [1, 2], [3, 4] ] = [ [1, 3], [2, 4] ]


# Function 1: Flip Array Horizontally
def flip_horizontally(array):
	if type(array[1]) is ListType:
		for item in array:
			item.reverse()
	else:
		array.reverse()

	return array


# Function 2: Flip Array Vertically
def flip_vertically(array):
	if type(array[1]) is ListType:
		array.reverse()

	return array


# Function 3: Transpose Array 
def transpose(array):
	transposed = []
	for item in array:
		if type(array[1]) is ListType:
			for i in range(0, len(item)):
				if i < len(transposed):
					transposed[i].append(item[i]) 
				else: 
					transposed.append([item[i]])
		else:
			transposed.append([item])
	return transposed


# Tests
print flip_horizontally([1,2]) #[2, 1]
print flip_horizontally([[1,2], [3,4]]) #[[2, 1], [4, 3]]
print flip_horizontally([[1,2,3], [4,5,6]]) #[3,2,1], [6,5,4]]

print flip_vertically([1,2]) #[1, 2]
print flip_vertically([[1,2], [3,4]]) #[[ 3, 4], [1 , 2]]
print flip_vertically([[1,2], [3,4], [5,6]]) #[[5,6], [3, 4], [1,2]]

print transpose([1,2]) #[[1], [2]]
print transpose([[1,2], [3,4]]) #[[1, 3], [2, 4]]
print transpose([[1,2], [3,4], [5,6]]) #[[1, 3, 5], [2, 4, 6]]

