# Input:
# s1 = "apple"
# s2 = "grape"

# Output: 3
# use set intersection for common char in string
s1 = "apple"
s2 = "grape"  

res = len(set(s1.lower()) & set(s2.lower()))
print(res)