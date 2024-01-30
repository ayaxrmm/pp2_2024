#ex.1
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: the set list is unordered, meaning: the items will appear in a random order.

#ex.2
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#ex.3
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#ex.4
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#ex.5
thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

#ex.6
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#ex.7
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#ex.8
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#ex.9
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item
print(thisset) #the set after removal

#ex.10
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#ex.11
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset) #this will raise an error because the set no longer exists

#ex.12
thisset = set(("apple", "banana", "cherry"))
print(thisset)
