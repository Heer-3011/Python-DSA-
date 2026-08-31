# Input : s = "geeksforgeeks"
#         c = 'e'
# Output : s = "gksforgks"

# Input : s = "geeksforgeeks"
#         c = 'g'

# def remove_char(str,char):
#     return str.replace(char,'')

def remove_char(s,c):
    str_n=[]
    for i in range(0,len(s)):
        str_n.append(s[i])
        if str_n[i]==c:
            str_n[i]=''
    return ''.join(str_n)

s = "geeksforgeeks"
c = 'e'

print(remove_char(s,c))