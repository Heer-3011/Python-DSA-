print("\n Hollow Square \n")
for i in range(1,5,1 ):
    for j in range(1,5,1):
        if i==1 or j==1 or i==4 or j==4 :
            print("*",end="") 
        else:
            print(" ",end="") 
    print()

print("Hollow Triangle\n")
n =4
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")
    
    # Print stars and internal spaces
    for j in range(1, (2 * i)):
        if j == 1 or j == (2 * i - 1) or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()