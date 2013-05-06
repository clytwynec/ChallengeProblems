# FizzBuzz rules:
# 	Print nums 1-100:
# 	 	if num divisible by 3, print Fizz
# 	 	if num divisible by 5, print BUzz 
# 	 	if num divisible by both, print FizzBuzz
# 	 	if none of the above, print num

# then.. add woof if divisible by 7 (with permutations FizzWoof, etc.)

import numpy as np
import sys

max_num = int(sys.argv[1])+1
nums = np.arange(0, max_num, 1)

# for num in nums:
# 	if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
# 		print 'FizzBuzzWoof'
# 	elif num % 3 == 0 and num % 5 == 0:
# 		print 'FizzBuzz'
# 	elif num % 3 == 0 and num % 7 == 0:
# 		print 'FizzWoof'
# 	elif num % 5 == 0 and num % 7 == 0:
# 		print 'BuzzWoof'
# 	elif num % 3 == 0:
# 		print 'Fizz'
# 	elif num % 5 == 0:
# 		print 'Buzz'
# 	elif num % 7 == 0:
# 		print 'Woof'
# 	else:
# 		print num

for num in nums:
	output = ''
	if num % 3 == 0:
		output += 'Fizz'
	if num % 5 == 0:
		output += 'Buzz'
	if num % 7 == 0: 
		output += 'Woof'
	if output == '': 
		output = num
	print output


