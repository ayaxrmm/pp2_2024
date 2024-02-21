def even_gener(n):
    for i in range(n+1):
        if i%2==0:
            print(i, end=", ") 
        else:
            continue
n=int(input("enter a number: "))
even_gener(n)

