#1example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 

#2example
for x in "banana":
  print(x) 

#3example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

#4example
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 

#5example
for x in range(6):
  print(x) 

#6example
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#7example
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
