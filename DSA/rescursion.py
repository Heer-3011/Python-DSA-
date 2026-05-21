def recursive(n): 
    if n <= 0:
        return 1
    print(n,end=" ")  
    recursive(n-1)  
recursive(5)