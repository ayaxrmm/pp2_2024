def prime(n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n%i==0:
                return False
        return True
def filter_prime(list):
    new=[]
    for i in list:
        if prime(i):
            new.append(i)
    return new
list=[1,2,3,4,5,6,7,11,13,14]
print(filter_prime(list))
