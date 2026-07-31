# Multiple Inheritance
    # When a class inherits from more than one base class, it is called multiple inheritance. 
    # The derived class inherits all features of its base classes.
    # In python, you can have more than one parent


# Syntax 
'''
    class Base1:
     # Body of the class
        pass

class Base2:
    # Body of the class
        pass

class Derived(Base1, Base2):
         # Body of the class
         pass 
'''

class Prey:
    def flee(self):
        print('This Animal is fleeing.')


class Predator:
    def hunt(self):
        print('This Animal is hunting.')


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass


class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# MRO 
# Method Resolution Order in Python Inheritance
    # Method Resolution Order (MRO) defines the order in which Python searches for a method in a class and its parent classes. 
    #  It becomes important when the same method exists in more than one class in an inheritance chain, especially in multiple inheritance.
    # The example shows how Python decides which method to execute when both a parent and a child class have a method with the same name.

class A:
    def fun(self):
        print('In Class A')

class B(A):
    def fun(self):
        print('In Class B')

a = B()
a.fun()

# Explanation:
# When obj.fun() is called, Python first looks in class B.
# Since B defines fun(), it runs that method and does not check class A.
# The MRO here is: B -> A.


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# 
# # THE DIAMOND PROBLEM
# In multiple inheritance, a child class can inherit from more than one parent class. When these parent classes come from a common base class, the structure forms a diamond shape and Python must decide which class method should be used.

class A:
    def fun(self):
        print("In class A")

class B(A):
    def fun(self):
        print("In class B")

class C(A):
    def fun(self):
        print("In class C")

class D(B, C):
    pass

a = D()
a.fun()
# D inherits from B and C.
# Python follows the MRO: D -> B -> C -> A.
# Since B has fun(), it is executed and the search stops.


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# C3 Linearization in MRO
# Python uses the C3 linearization algorithm to decide the order in which classes are searched when a method is called.
# This algorithm produces a single, consistent order that respects both inheritance and the order in which parent classes are written.


class A:
    def fun(self):
        print("In class A")

class B(A):
    def fun(self):
        print("In class B")

class C(A):
    def fun(self):
        print("In class C")

class D(B, C):
    pass

obj = D()
obj.fun()

print(D.__mro__)


# Explanation:
# When obj.fun() is called, Python follows the MRO shown by D.__mro__.
# It checks D, then B, then C, then A.
# Since B defines fun(), that method is executed and the search stops.

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# Methods to View Method Resolution Order (MRO) of a Class
# Python provides two ways to check the method resolution order (MRO) of a class:

# __mro__ attribute: shows a tuple of classes in the order Python searches for methods.
# mro() method: returns a list of classes in the MRO.

class A:
    def fun(self):
        print("In class A")

class B:
    def fun(self):
        print("In class B")

class C(A, B):
    def __init__(self):
        print("Constructor C")

obj = C()

print(C.__mro__) 
print(C.mro())

# C.__mro__ returns the method resolution order as a tuple.
# C.mro() returns the same order as a list.
# This sequence shows that Python will search C, then A, then B, and finally object when resolving any method call.

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# MIXINS IN PYTHON

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
# if we add serialize method here in shape class than shape class has more than one responsibility. shape distribution and serialization which is not correct!
class Serialization:
    def serialize(self): #this is mixin
        pairs  = []
        for k,v in self.__dict__.items():
            pairs.append(f'{k} = {v}')
        result = ','.join(pairs)
        print(result)


class Rectange(Shape,Serialization):
    def __init__(self, x, y,width,height):
        super().__init__(x, y)

        self.width = width 
        self.height = height


class Circle(Shape,Serialization):
    def __init__(self, x, y,radius):
        super().__init__(x, y)

        self.radius = radius


r = Rectange(0,0,100,50)
c = Circle(0,0,40)
r.serialize()
c.serialize()