def speaksay(n):
	if n == 1:
		return 1
	else:
		prev = speaksay(n - 1)

		last_num = 0
		count = 0
		result = 0
		while prev > 0: 
			end_place = prev % 10;
			prev /= 10

			print end_place, prev

			if end_place == last_num:
				count += 1
				last_num = end_place
			else:
				result *= 100
				result += count * 10 + last_num

				count = 1
				last_num = end_place

			print last_num, count

		result *= 100
		result += count * 10 + last_num
		return result

import sys

print speaksay(int(sys.argv[1]))