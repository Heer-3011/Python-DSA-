# text = "apple orange banana"
# words_to_replace = ["apple", "banana"]
# Output: "K orange K"

def replace(text,replace):
    str1=text.split()
    for i in range(0,len(str1)):
        if str1[i] in replace:
            str1[i]="K" 
    return ' '.join(str1)
        

text = "apple orange banana"
words_to_replace = ["apple", "banana"]

print(replace(text,words_to_replace))