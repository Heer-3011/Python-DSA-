# Given a list of integers, the task is to identify and 
# print all elements that appear more than once in the list.
#  For Example: Input: [1, 2, 3, 1, 2, 4, 5, 6, 5],
#  Output: [1, 2, 5]. Below are several methods to print duplicates from a list in Python.
a = [1, 2, 3, 1, 2, 4, 5, 6, 5]
dup = []

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j] and a[i] not in dup:
            dup.append(a[i]) 
print(dup)     
