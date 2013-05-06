
def find_fib_num(n):
	if n==0:
		return 0
	elif n==1:
		return 1  
	else:
		return find_fib_num(n-1) + find_fib_num(n-2)

print 'find_fib_num'
print find_fib_num(0)
print find_fib_num(1)
print find_fib_num(5)
print find_fib_num(30)


a = (1.0 + 5.0**(0.5))/2.0 
b = (1.0 - 5.0**(0.5))/2.0

def fib(n):
	return int((a**n - b**n)/(5.0**(0.5)))

print 'fib'
print fib(0)
print fib(1)
print fib(5)
print fib(30)