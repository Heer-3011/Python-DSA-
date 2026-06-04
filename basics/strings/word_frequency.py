# Input: "hello world hello everyone"
# Output: {'hello': 2, 'world': 1, 'everyone': 1}

str="hello world hello everyone"
dict1={}
str_list=str.split()

for i in str_list:
    dict1[i]=str_list.count(i)

print(dict1)

 
