def reverse_string(s):
    d=s[::-1]
    if s==d:
        return True, d
    else:
        return False, d
s=input("enter a string: ")
print(reverse_string(s))
