# Given a string s, the task is to check if it is palindrome or not.

# Example:
# Input: s = "abba"
# Output: true
# Explanation: s is a palindrome 

def palidrone(str): 
    return str[-1:-len(str)-1:-1]==str

print(palidrone('abba'))

