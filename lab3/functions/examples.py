#1example
def my_function():
  print("Hello from a function")

my_function()

#2example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#3example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#4example
def my_function(x):
  return x*5
print(my_function(3))
print(my_function(5))
print(my_function(9))

#5example
def tri_recurtion(k):
  if (k>0):
    result = k+tri_recurtion(k-1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recurtion(6)

