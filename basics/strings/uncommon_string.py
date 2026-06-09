# A = "Geeks for Geeks"
# B = "Learning from Geeks for Geeks"
# Output: ['Learning', 'from'].

def uncommon(s1,s2): 
    res=list(set(s1.split()) ^ set(s2.split()))
    return res


a = "Geeks for Geeks"
b = "Learning from Geeks for Geeks"
print(uncommon(a,b))