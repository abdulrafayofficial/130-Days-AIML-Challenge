import time
#default Arguments: A default value for certain parameters
#make your functions more flexible, reduces number of arguments
#Non-default arguments follow default arguments

def netPrice(list_price , discount=0 , tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(netPrice(500,0,0.05))
print(netPrice(500))
print(netPrice(500,0.1))

#Another example:

def count(end , start=0):
    for x in range(start , end+1):
        print(x)
        # time.sleep(1)

count(10)


#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------


# *args    = allows you to pass multiple non-key arguments. In *args the function will receive a tuple of arguments and can access the items accordingly.

#         *unpacking Operator


def addNumbers(*numbers):
    total = 0
    for num in numbers:
        total += num
        
    return total

print(addNumbers(1,2,3,43,54,98,342,121))


#---------------

def myKids(*kids):
    print("Youngest kid is : ",kids[2])

myKids("Abdul","Rafay","Rayaan")# we can add as many arguments

#---------------

def myfunction(*args):
    print("Type:",type(args))
    print("First Value:", args[0])
    print("Second Value:", args[1])
    print("Third Value:", args[2])

myfunction("Hello","Abdul","Rafay")

#---------------

def my_function(greeting, *names):
    for x in names:
        print(greeting, x)
my_function("hello","Rafay","Rayyaan","Abdullah","Hasan")


#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

# **kwargs = allows you to pass multiple keyword arguments. In **kwargs, the function will receive a dictionary of arguments and can access the items accordingly.

def print_address(**kwargs):
    # for key in kwargs.keys():
    #     print(key)

    # for value in kwargs.values():
    #     print(value)

    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="F-type Main st.",
              city="Sadiqabad",  
              state="None", 
              zip="12345",)


def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print( key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


def myFunction(title , *args , **kwargs):
    print("Title: ",title)
    print("*args: ", args)
    print("**kwargs:", kwargs)

myFunction("Information","Abdul","Rafay",
            Age=22,
            hobby="Coding",
            Fav_lang="Python",
            is_Student= True)


#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

#Lambda Functions
# A lambda function is a small anonymous function.--- no need to name it..!

# Syntax 
# lambda arguments : expression

x = lambda x: x*2
print(x(5))

#it can take any number of arguments!...

x = lambda a,b: a*b
print(x(5,5))

check = lambda i: i in "python"
print(check("t"))
print(check("u"))

#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

#Higher Order Functions: a function that either: 
                        # 1.accepts a function as an argument
                            # or 
                        # 2. Returns a function 
                        # (In python functions are also treated as objects)

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)
    
hello(loud)
hello(quiet)

#----------------------------

def divisor(x):
    def dividend(y):  
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))

