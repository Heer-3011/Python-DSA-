str="My name is Heer patel"

str1=str.split() 
even= [w for w in str1 if len(w)%2==0]
result=' '.join(even)
print(result)