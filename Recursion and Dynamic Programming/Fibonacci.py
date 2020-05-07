'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.

'''


# recursive 


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N -1) + self.fib(N-2)
        
'''
Time complexity : o(2^n)
 This is the slowest way to solve the Fibonacci Sequence because it takes exponential time. 
 The amount of operations needed, for each level of recursion, grows exponentially as the depth approaches N.

Space complexity : o(n)
  We need space proportionate to N to account for the max size of the stack, in memory. 
  This stack keeps track of the function calls to fib(N). 
  This has the potential to be bad in cases that there isn't enough physical memory to handle the increasingly growing stack, leading to a StackOverflowError.
'''


#iterative 


class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        a = 0
        b = 1
        
        while N > 1:
            tot = a + b
            a = b
            b = tot
            N -= 1
        return b


'''
Time: 0(n)
Space 0(n)

'''


# dynamic programming 

# Fibonacci Series using Dynamic Programming 
def fibonacci(n): 
	
	# Taking 1st two fibonacci nubers as 0 and 1 
	FibArray = [0, 1] 
	
	while len(FibArray) < n + 1: 
		FibArray.append(0) 
	
	if n <= 1: 
		return n 
	else: 
		if FibArray[n - 1] == 0: 
			FibArray[n - 1] = fibonacci(n - 1) 

		if FibArray[n - 2] == 0: 
			FibArray[n - 2] = fibonacci(n - 2) 
			
	FibArray[n] = FibArray[n - 2] + FibArray[n - 1] 
	return FibArray[n] 
	
print(fibonacci(9)) 
