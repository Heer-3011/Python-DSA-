# Input : str = "hello geeks for geeks 
#           is computer science portal" 
#         k = 4
# Output : hello geeks geeks computer 
#          science portal
# Explanation : The output is list of all 
# words that are of length more than k

def greater(str,k):
    words=str.split() 
    str_result=' '.join([i for i in words if len(i)>k ])
    return str_result
str = "hello geeks for geeks is computer science portal" 
print(greater(str,4))

