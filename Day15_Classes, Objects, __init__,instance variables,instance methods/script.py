class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)

# -------------------------------------------------------------------
# Delete Objects
# You can delete objects by using the del keyword:

del p1

# -------------------------------------------------------------------
# Multiple Objects

p2 = MyClass()
p3 = MyClass()
p4 = MyClass()

print(p2.x)
print(p3.x)
print(p4.x)
# -------------------------------------------------------------------
# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
    pass

# -------------------------------------------------------------------

# Python __init__() Method

# __init() aik aisa method hai jo automatically chalta hai jab ham class se objects banate hain..aur is ka kaam hota hai us object ka starting data set karna


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('AbdulRafay',22)
print(p1.name , p1.age)


# withour __init__():

class Car:
    pass

C1 = Car()
C1.name = 'Corolla'
C1.color = 'white'

print(C1.name)
print(C1.color)

# Using __init__() makes it easier to create objects with initial values:

# Default Values in __init__()

class Student:
    def __init__(self,name,roll=38):
        self.name = name
        self.roll = roll

s1 = Student('AbdulRafay')
s2 = Student('GGGGG', 27)

print(s1.name)
print(s1.roll)
print(s2.name)
print(s2.roll)


# Multiple Parameters

class Man:
    def __init__(self,name,age, city , country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

m1 = Man('AbdulRafay',22,'sadiqabad','Pakistan')
print(m1.name, m1.age, m1.city, m1.country)

# -------------------------------------------------------------------

# Python self Parameter

# The self Parameter
# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.

class Info:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print('Hello my name is : '+ self.name)

A1 = Info('AbdulRafay',22)
print(A1.name , A1.age)
A1.greet()


class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()


# Calling Methods with self

class Person:
    def __init__(self,name):
        self.name = name

    def greet(self):
        return f'Hello {self.name}! '
    
    def welcome(self):
        message = self.greet()
        print(message + 'Welcome to Our Team!!...')

p7 = Person('Abdul')
p7.welcome()


# Example: Class Variable vs Instance Variable

class CSStudent:
    stream = 'cse'          # Class variable

    def __init__(self, name, roll):
        self.name = name    # Instance variable
        self.roll = roll    # Instance variable

# Creating objects
a = CSStudent('Rose', 1)
b = CSStudent('Nat', 2)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)