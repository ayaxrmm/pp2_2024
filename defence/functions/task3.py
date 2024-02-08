def get_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
print(get_max(a,b,c))
