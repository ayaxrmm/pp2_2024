#1 example
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2example
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#3example
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"
# the value is still the same:
print(thistuple)

#4 example
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#5example
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#6example
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#7example
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#8example
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

