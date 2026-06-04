# Input: "education"
# Output: True

# Input: "geeksforgeeks"
# Output: False

str="education"
str1='geeksforgeeks'
def vowels(str):
    if 'a' and 'e' and 'i' and 'e' or 'u' in str:
        print(True)
    else:
        print(False)

vowels(str.lower)