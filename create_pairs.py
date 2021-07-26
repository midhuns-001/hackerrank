#Example test:   [1, 2, 2, 1] - True

#Example test:   [7, 7, 7] - False
#Example test:   [1, 2, 2, 3] False

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    dict = {}
    for i in A:
        if i in dict.keys():
            dict[i] = dict[i]+1
        else:
            dict[i] = 1
    for key,value in dict.items():
        if ((value % 2) != 0):
            return False
        else:
            return True
        
