#create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#access list items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#change the value of a list item
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)

#loop through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#check if a list item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#length of a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#add an item to the end of a list
thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)

#add an item to the specified index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#remove an item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#remove an item to the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#empty a list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#use list()
thislist = list(("apple", "banana", "cherry"))
print(thislist)
