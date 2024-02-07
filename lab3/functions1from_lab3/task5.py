s=input("enter a string: ")
def permituation(s,c=""):
    if len(s) == 0:
        print(c)
    else:
        for i in range(len(s)):
            char=s[i]
            remining=s[:i]+s[i+1:]
            permituation(remining, c+char)
print("permituations of the string: ")
permituation(s)

