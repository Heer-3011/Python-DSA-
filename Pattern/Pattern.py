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
 