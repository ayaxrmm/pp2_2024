def is_prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15]
b=list()
for i in a:
    if is_prime(i):
        b.append(i)
    else:
        continue
for i in b:
    print(i)

    
