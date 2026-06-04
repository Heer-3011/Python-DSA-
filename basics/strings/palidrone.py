# Input: "madam"  
# Output: Palindrome  

name="madam"
name2="heer"
def palidrone(str):
    str1=str[::-1]
    if str1==str:
        return "Palidrone"
    else:
        return "Not a palidrone"
    
print(palidrone(name2))

def Symmetrical(str):
    half=len(str)//2
    sym=str[:half] == str[half:] if len(str)%2==0 else str[:half] == str[half+1:]
    print(sym)

Symmetrical("abcab")