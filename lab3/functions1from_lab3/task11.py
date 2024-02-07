def is_polindrome(s):
    d=s[::-1]
    if d!=s:
        return False
    return True
s=input("enter a string: ")
print(is_polindrome(s))