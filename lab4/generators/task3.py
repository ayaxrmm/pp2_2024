def func_generator(n):
    for i in range(1, n+1):
        if i%3==0 and i%4==0:
            print(i, end=", ")
        else:
            continue
n=int(input())
func_generator(n)
