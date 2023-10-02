# this code is about the max subset sum no adjacent 


def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0 
    elif len(array) ==1:
        return array[0]

    second = array[0]
    first = max(array[0] , array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current 
    return first
    
    
# Your code is a concise implementation of the dynamic programming approach to solve the Maximum 
# Subset Sum with No Adjacent Elements problem.

# The approach starts by initializing two variables second and first to represent the maximum sum 
# of a subset with no adjacent elements up to the second-last and last elements of the array, respectively.

# Then, the loop iterates through the array starting from the third element, and for each element, 
# it computes the maximum sum of a subset with no adjacent elements up to that element, using the
# recurrence relation current = max(first, second + array[i]).

# After computing current, the code updates second and first by shifting their values by one position
# to the right, so that second becomes the previous value of first, and first becomes the current value of current.

# Finally, the code returns first, which represents the 
# maximum sum of a subset with no adjacent elements in the entire array.