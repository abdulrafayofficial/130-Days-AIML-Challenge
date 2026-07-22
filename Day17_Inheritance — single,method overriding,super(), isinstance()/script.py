#                                 Python Inheritance
# -Inheritance allows us to define a class that inherits all the methods and properties from another class.
#         Parent class is the class being inherited from, also called base class.
#         Child class is the class that inherits from another class, also called derived class.


class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)



# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
    # We want to add the __init__() function to the child class (instead of the pass keyword).
    def __init__(self, fname, lname):
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
        Person.__init__(self,fname,lname)
    # Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.




p1 = Person('Abdul','Rafay')
p1.printname()

s1 = Student('Abdul','Wasay')
s1.printname()

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------

# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

class Fruits:
    def __init__(self,name,color,taste):
        self.name = name
        self.color = color
        self.taste = taste

    def define_taste(self):
        print(f'{self.name} is of {self.color} color and has a {self.taste} taste')

class Mango(Fruits):
    def __init__(self, name, color, taste,is_good):
        super().__init__(name,color,taste)
        # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
        self.is_good = is_good

        # Add Methods
        # If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

    def define_taste(self):
            print(f'{self.name} is the KING of Fruits. Taste: {self.taste}')
        

m1 = Mango('Mango','yellow','Sweet',True)
print(m1.is_good)
m1.define_taste()
f1 = Fruits('Apple','red','sour')
f1.define_taste()

#----------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------- 

# isinstance()

# Python isinstance() Function

x = isinstance(5,int)
print(x)
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

# Syntax:
#     isinstance(object, type)

print(isinstance(m1, Mango))    # True — m1 Mango ka object hai
print(isinstance(m1, Fruits))   # True — Mango, Fruits se inherit karta hai, isliye yeh bhi True!
print(isinstance(f1, Mango))    # False — f1 sirf Fruits ka object hai, Mango ka nahi