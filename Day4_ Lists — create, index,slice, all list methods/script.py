#Lists

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.
#List items can be of any data type

mylist1  = ["apple", "banana", "cherry"]
print(mylist1)

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


#List Length

mylist2 = ["apple", "banana", "cherry"]
print(len(mylist2))

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


#List Items - Data Types
#list can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

#Access Items

mylist3 = ["apple", "banana", "cherry"]
print(mylist3[1]) #---> banana on index1 will be printed

# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

mylist4 = ["apple", "banana", "cherry"]
print(mylist4[-1])

#Range of Indexes
mylist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist5[2:5])
print(mylist5[:4])
print(mylist5[2:])
print(mylist5[-4:-1])


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

#Check if Item Exists

mylist6 = ["apple", "banana", "cherry"]
if "apple" in mylist6:
  print("Yes, 'apple' is in the fruits list")

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

#Change Item Value
mylist7 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist7[1] = "blackcurrant"
print(mylist7)
mylist7[1:3] = ["blackcurrant", "watermelon"]
print(mylist7)

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

#Python - Add List Items

# To insert a new list item,< without replacing any of the existing values > , we can use the insert() method.
# The insert() method inserts an item at the specified index:

mylist8 = ["apple", "banana", "cherry"]
mylist8.insert(2, "watermelon")
print(mylist8)


# Append Items
# To add an item to the end of the list, use the append() method:
mylist9 = ["apple", "banana", "cherry"]
mylist9.append("orange")
print(mylist9)


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

# Python - Remove List Items

# The remove() method removes the specified item
# If there are more than one item with the specified value, the remove() method removes the first occurrence:

mylist10 = ["apple", "banana", "cherry"]
mylist10.remove("banana")
print(mylist10)


# The pop() method removes the specified index.
# If you do not specify the index, the pop() method removes the last item.
mylist11 = ["apple", "banana", "cherry"]
mylist11.pop(1)
print(mylist11) #--> banana will be removed


#The del keyword also removes the specified index:
# The del keyword can also delete the list completely.

mylist12 = ["apple", "banana", "cherry"]
del mylist12[0]
print(mylist12)

mylist12 = ["apple", "banana", "cherry"]
del mylist12
# print(mylist12) --> this will give an error --> mylist12' is not defined


# Clear the List
# The clear() method empties the list. The list still remains, but it has no content.
mylist13 = ["apple", "banana", "cherry"]
mylist13.clear()
print(mylist13)

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


# Looping through a List

mylist14 = ["apple", "banana", "cherry"]
for x in mylist14:
  print(x)

#Using a While Loop

i = 0
while i< len(mylist14):
    print(mylist14[i])
    i +=1

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#Common way:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for fruit in fruits:
   if "a" in fruit:
      new_list.append(fruit)

    
print(new_list)

#using list Comprehension:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [fruit for fruit in fruits if "a" in fruit]
print(new_list)
#newlist = [expression for item in iterable if condition == True]


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# Python - Sort Lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Python - Copy Lists
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)