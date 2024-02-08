def word_fricuence(text):
    words=text.split()
    fric_dict={}
    for i in words:
        if i in fric_dict:
            fric_dict[i]+=1
        else:
            fric_dict[i]=1
    return fric_dict
text=input()
print(word_fricuence(text))