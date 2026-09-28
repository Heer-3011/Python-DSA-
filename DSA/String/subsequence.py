# Input: s1 = "AXY", s2 = "ADXCPY"
# Output: true 
# Explanation: All characters of s1 are in s2 in the same order

# Input: s1 = "AXY", s2 = "YADXCP"
# Output: false 
# Explanation: All characters are present, but order is not same.

# Input: s1 = "gksrek", s2 = "geeksforgeeks"
# Output: true

def subsequence(str1, str2):
    j = 0

    for i in range(len(str2)):
        if j < len(str1) and str1[j] == str2[i]:
            j += 1

    return j == len(str1)


s1 = "AXY"
s2 = "ADXCPY"
print(subsequence(s1, s2))

s1 = "AXY"
s2 = "YADXCP"
print(subsequence(s1, s2))

s1 = "gksrek"
s2 = "geeksforgeeks"
print(subsequence(s1, s2))