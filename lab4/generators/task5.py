def generator(n):
    while n>=0:
        yield n
        n-=1
n=int(input("enter a number n: "))
for i in generator(n):
    print(i)
