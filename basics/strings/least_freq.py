# input:GeeksforGeeks
# output:f

str1="GeeksforGeeks"
dict1={}
for i in str1:
    dict1[i]=str1.count(i)
print(dict1)
res = min(dict1, key=dict1.get)
print(str(res))