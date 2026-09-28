# Input:  s = "g  eeks   for ge  eeks  "
# Output: geeksforgeeks
# Explanation: All the spaces have been removed.

# Input:  s = "   abc d "
# Output: abcd
# Explanation: All the spaces including the leading ones have been removed.

def space(str):
    print(str)
    return ''.join(str.split())

s = "   abc d "
print(space(s))