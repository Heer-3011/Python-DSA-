print("\n Number Triangle Pattern\n")  
for i in range(1,5,1):
    for j in range(1,i,1):
        print(j,end="")
    print(i)

print("\n Inverted Number Triangle Pattern\n")  
for i in range(5,1,-1):
    for j in range(1,i,1):
        print(j,end="")
    print(" ")

print("\n Same Number Triangle Pattern\n")  
for i in range(1,5,1):
    for j in range(1,i,1):
        print(i,end="")
    print(i)

print("\n Floyd’s  Triangle Pattern\n") 
a=0
for i in range(1,6,1):
    for j in range(1,i,1):
        a+=1
        print(" ",a,end="")
    print(" ")