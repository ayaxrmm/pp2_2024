#1example
a = 33
b = 200

if b > a:
  print("b is greater than a")

#2example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#3example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#4example
a = 200
b = 33

if a > b: print("a is greater than b")

#5example
a=2
b=330
print("A") if a>b else print("B")

#6example
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#7example
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
