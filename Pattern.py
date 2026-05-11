# print("\nSquare Pattern\n") 
# for i in range(1,5,1):
#     for j in range(1,4,1):
#         print("*" ,end=" ")
#     print("*")

# print("\n\n Right-Angled Triangle\n") 
# for i in range(1,5,1):
#     for j in range(1,i,1):
#         print("*",end="")
#     print("*")

# print("\nInverted Right Triangle\n")
# for i in range(5,1,-1):
#     for j in range(i,1,-1):
#         print("*",end="")
#     print("")

print("\n Pyramid Pattern\n")
 
for i in range(0, 4 ):
    spaces = 4 - i
    stars = 2 * i + 1 
                                                     
    print(" " * spaces + "*" * stars)    

print("\n Inverted Pyramid Pattern\n")
 
for i in range(4,0,-1):
    spaces = 4 - i
    stars = 2 * i - 1 
                                                     
    print(" " * spaces + "*" * stars)  

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

print("\n Alphabet  Triangle Pattern\n") 
a=0
for i in range(1,6,1):
    for j in range(0,i,1):
        print(chr(65+j),end=" ")
    print()

print("\n Inverted Alphabet  Triangle Pattern\n") 
a=0
for i in range(4,0,-1):
    for j in range(0,i,1):
        print(chr(65+j),end=" ")
    print()

print("\n Same Alphabet  Triangle Pattern\n") 
for i in range(0,5,1):
    for j in range(0,i,1):
        print(chr(64+i),end=" ")
    print()

print("\n Continous Alphabet  Triangle Pattern\n") 
for i in range(0,5,1):
    for j in range(0,i,1):
        a+=1
        print(chr(64+a),end=" ")
    print()

print("\n Alternating 1 & 0 Pattern \n")
a=1
for i in range(0,5,1):
    for j in range(0,i,1): 
        if a==0:
            print(a,end=" ")
            a=1
        else:
            print(a,end=" ")
            a=0 
    print()

print("\n Star + Number Pattern\n")
for i in range(0,4,1):   
    print("*"* i,i+1 )

print("\n Hollow Square \n")
for i in range(1,5,1 ):
    for j in range(1,5,1):
        if i==1 or j==1 or i==4 or j==4 :
            print("*",end="") 
        else:
            print(" ",end="") 
    print()

print("\n Diamond  pattern \n")
for i in range(0,5,1):
    spaces=4-i
    stars=2*i-1

    print(" "* spaces+"*"*stars)
for i in range(4,0,-1):
    spaces=4-i
    stars=2*i-1

    print(" "* spaces+"*"*stars)



print("\n Reverse Pyramid Numbers\n") 
for i in range(4): 
    for j in range(i):
        print(" ", end="") 
    for j in range(i, 4):
        print(j + 1, end="")
    print()

print("\n Palindrome number pattern\n")
for i in range(1,5,1): 
    for j in range(1,i):
        print(j,end="")
    for k in range(i,0,-1): 
            print(k,end="") 
    print()
 