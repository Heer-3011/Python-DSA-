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
