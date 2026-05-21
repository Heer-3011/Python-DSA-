# Given an array of size N, find the sum of its elements.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints:
# 1 <= n <= 100000
# -10000 <= ai <= 10000
# Output Format
# In single line, print one integer : sum of all the elements in the array
# Sample Input 1:
# 5
# 1 2 3 4 5 
# Sample Output 1:
# 15
def sum(arr):
    sum=0
    for i in range(0,len(arr)) :
        sum+=arr[i]
    return sum

n = int(input( ))

arr = list(map(int, input( ).split()))
print(sum(arr))