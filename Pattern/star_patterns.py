print("\nSquare Pattern\n") 
for i in range(1,5,1):
    for j in range(1,4,1):
        print("*" ,end=" ")
    print("*")

print("\n\n Right-Angled Triangle\n") 
for i in range(1,5,1):
    for j in range(1,i,1):
        print("*",end="")
    print("*")

print("\nInverted Right Triangle\n")
for i in range(5,1,-1):
    for j in range(i,1,-1):
        print("*",end="")
    print("")

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
