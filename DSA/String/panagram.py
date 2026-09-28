# Input: s = "The quick brown fox jumps over the lazy dog" 
# Output: true
# Explanation: The input string contains all characters from 'a' to 'z'.

# Input: s = "The quick brown fox jumps over the dog"
# Output: false
# Explanation: The input string does not contain all characters from 'a' to 'z', as 'l', 'z', 'y' are missing
import string
def panagram(str1):
    str1=str1.lower()
    str2=[char for char in str1]
    list1=list(string.ascii_lowercase) 
    for i in range(0,len(list1)):
        if str2.__contains__(list1[i]) != True:
            return False
    return True 


print(panagram("The quick brown fox jumps over the lazy dog"))
 