def squares(a,b):
    for i in range(a, b+1):
        yield i**2
a=int(input("enter a number a: "))
b=int(input("enter a number b: "))
for i in squares(a,b):
    print(i)
