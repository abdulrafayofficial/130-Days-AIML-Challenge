# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicates are not allowed in sets:
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Python - Access Set Items

# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

# Check if "banana" is present in the set:

thisset = {"apple", "banana","cherry"}
print("banana" in thisset)

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# Python - Add Set Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Add Sets
# To add items from another set into the current set, use the update() method.

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


#Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# Python - Join Sets

# The union() and update() methods joins all items from both sets.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)


#Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)


# Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


# #Intersection
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# You can use the & operator instead of the intersection() method, and you will get the same result.
# set3 = set1 & set2

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)



# Difference
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# You can use the - operator instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)


# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
