# Strings

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1]) #---> e would be the answer bcz index start from 0

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


# Looping Through a String

b = "Abdul Rafay"
for x in b:
    print(x, end= "")
print()

# String Length

c = "Abdul Wasay"
print(len(c))


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

# Check String

txt = "The best things in life are free!"
print("free" in txt) # ---> true

# Check if NOT

txt = "The best things in life are free!"
print("expensive" not in txt)


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

# Python - Slicing Strings

'''
You can return a range of characters by using the slice syntax.
Specify the start index and the end index, separated by a colon, to return a part of the string.
'''

d = "Hello, World!"
print(d[2:5]) # llo will be printed the second digit(after the colon is exclusive)

e = "Hello, World!"
print(e[:5])

f = "Hello, World!"
print(f[2:])

g = "Hello, World!"
print(g[-5:-2])

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

# Python - Modify Strings

# Upper Case

h = "i love Python!"
print(h.upper())

# Lower Case

i = "Hello, World!"
print(i.lower())

# Remove Whitespace
# The strip() method removes any whitespace from the beginning or the end:
j = "    Hello, World!      "
print(j.strip()) # returns "Hello, World!"


# Replace String

k = "Hello, World!"
print(k.replace("H", "J"))

# Split String
# The split() method splits the string into substrings if it finds instances of the separator:

l = "Hello, World!"
print(l.split(",")) # returns ['Hello', ' World!']



#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

# Python - String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

a = "Intelligent"
b = " boy"
c = a + b
print(c)

# Python - Format - Strings

age = 22
txt = f"My name is Abdul Rafay, I am {age}"
print(txt)

# A placeholder can include a modifier to format the value.
# Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

# Python - Escape Characters
# An escape character is a backslash \ followed by the character you want to insert.

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."



#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

#---------------STRING METHODS-----------------------

#1. CAPITALIZE()
# The first character is converted to upper case, and the rest are converted to lower case:
txt = "python is FUN!"
x = txt.capitalize()
print (x)

#2.casefold() METHOD IS SIMILAR TO lower()method... but a bit stronger....it lowercase the string

# 3. center()
# it takes 2 parameters, length and character(which is optional)
txt = "banana"
x = txt.center(20, "-")
print(x)

# 4. count() ----> Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# to see more see under python reference in w3 school python portion

