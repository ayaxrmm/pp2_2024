def f_to_c(n):
    c = (5/9) * (n-32)
    return c
F=int(input("enter Fahrenheit temperature: "))
ctemp = f_to_c(F)
print("Fahrenheit temperature to centigrade: ", ctemp)
