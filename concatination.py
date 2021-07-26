
'''
Given an array A consisting of N strings, calculates the length of the longest string S fulfilling the conditions above.

'''
#Example test:   ['co', 'dil', 'ity']  - 5
#Example test:   ['abc', 'yyy', 'def', 'csv'] 


# Python3 program to implement
# the above approach

# Function to check if all the
# string characters are unique
def check(s):
	
	a = set()

	# Check for repetation in
	# characters
	for i in s:
		if i in a:
			return False
			
		a.add(i)

	return True

# Funcyion to generate all possible
# strings from the given array
def helper(arr, ind):

	# Base case
	if (ind == len(arr)):
		return [""]

	# Consider every string as
	# a starting substring and
	# store the generated string
	tmp = helper(arr, ind + 1)

	ret = tmp

	# Add current string to result of
	# other strings and check if
	# characters are unique or not
	for i in tmp:
		test = i + arr[ind]
		
		if (check(test)):
			ret.append(test)

	return ret
	
# Function to find the maximum
# possible length of a string
def solution(arr):

	tmp = helper(arr, 0)

	l = 0

	for i in tmp:
		l = l if l > len(i) else len(i)

	return l

# Driver Code
if __name__=='__main__':
	
	s = []
	s =["co", "dil", "ity"]
	#s.append("abcdefgh")
	print(maxLength(s))
	print(s)


