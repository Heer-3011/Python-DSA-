# Input : s = "geeksForgEeks"
# Output : "GEEKSfORGeEKS"
# Explanation : All lower case characters are changed into upper case and vice versa.

# Input : s = "SMALLcase"
# Output : "smallCASE"
# Explanation : All lower case characters are changed into upper case and vice versa.

def toggle_case(str): 
    str_n=[]
    for i in range(0,len(str)):
        str_n.append(str[i]) 

        if str_n[i].isupper():
            str_n[i]=str_n[i].lower()
        elif str_n[i].islower():
                    str_n[i]=str_n[i].upper()
                    
    return ''.join(str_n)

print(toggle_case('geeksForgEeks'))
print(toggle_case('SMALLcase'))