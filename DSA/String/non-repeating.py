# Input: s = "geeksforgeeks"
# Output: 'f'
# Explanation: 'f' is the first character in the string which does not repeat.

# Input: s = "racecar"
# Output: 'e'
# Explanation: 'e' is the only character in the string which does not repeat.

# Input: "aabbccc"
# Output: '$'
# Explanation: All the characters in the given string are repeating.

def nonrepeating(str1):
    str2=[char for char in str1] 
    for i in range(0,len(str2)):
        if str2.count(str2[i]) == 1:
            return str2[i]
    return '$'   
print(nonrepeating('geeksforgeeks'))
print(nonrepeating('racecar'))
print(nonrepeating('aabbccc'))

