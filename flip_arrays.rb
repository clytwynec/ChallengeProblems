# write three functions to perform the following operations on a 2 dimensional array:
# 1) flip the array horizontally
# 2) flip the array vertically
# 3) transpose the array
# Examples
# 1) e.g. [1, 2] => [2, 1] or [ [1, 2], [3, 4] ] => [ [2, 1], [ 4, 3] ]
# 2) e.g. [1, 2] => [1, 2] (flipping a 2x1 matrix vertically should keep it the same), [ [1, 2], [3, 4] ] => [ [ 3, 4], [1 , 2] ]
# 3) e.g. [1, 2] => [ [1], [2] ] (2x1 becomes 1x2) or [ [1, 2], [3, 4] ] = [ [1, 3], [2, 4] ]


# Function 1: Flip Array Horizontally
def flip_horizontally(array)
	if array[1].kind_of?(Array)
		for item in array
			item.reverse!
		end
	else 
		array.reverse!
	end
	return array
end


# Function 2: Flip Array Vertically
def flip_vertically(array)
	if array[1].kind_of?(Array)
		array.reverse!
	end

	return array
end


# Function 3: Transpose Array 
def transpose(array)
	transposed = []

	for item in array
		if item.kind_of?(Array)
			for i in (0... item.count)
				if i < transposed.count
					transposed[i].push(item[i]) 
				else 
					transposed.push([item[i]])
				end
			end
		else
			transposed.push([item])
		end
	end

	return transposed
end



# Tests
print flip_horizontally([1,2])#[2, 1]
print "\n"
print flip_horizontally([[1,2], [3,4]]) #[[2, 1], [4, 3]]
print "\n"
print flip_horizontally([[1,2,3], [4,5,6]]) #[3,2,1], [6,5,4]]
print "\n"

print flip_vertically([1,2]) #[1, 2]
print "\n"
print flip_vertically([[1,2], [3,4]]) #[[ 3, 4], [1 , 2]]
print "\n"
print flip_vertically([[1,2], [3,4], [5,6]]) #[[5,6], [3, 4], [1,2]]
print "\n"

print transpose([1,2]) #[[1], [2]]
print "\n"
print transpose([[1,2], [3,4]]) #[[1, 3], [2, 4]]
print "\n"
print transpose([[1,2], [3,4], [5,6]]) #[[1, 3, 5], [2, 4, 6]]
print "\n"