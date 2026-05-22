# Given an array of integers, the task is to check whether it is monotonic.
#  A monotonic array is an array that consistently increases or decreases.

# Monotone Increasing: Every element is less than or equal to the next one (A[i] ≤ A[i+1]).
# Monotone Decreasing: Every element is greater than or equal to the next one (A[i] ≥ A[i+1]).
# Return: True if the array is monotonic, otherwise False.

# For Examples:
# Input: [6, 5, 4, 4] -> Output: True
# Input: [5, 15, 20, 10] -> Output: False
def monotonic(arr):
    inc_arr=sorted(arr)
    dec_arr=sorted(arr,reverse=True)
    result=inc_arr==arr or dec_arr==arr
    return result
 
arr=[30,40,50]
print(monotonic(arr))