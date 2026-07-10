# module = a file containing code you want to include in your program.
        # use import to include a module(built-in or your own)
        # useful to breakup a large program reusable seperate files.
'''
import math
print(math.pi)
print(math.e)
'''
#----------------------
'''
#using as alias
import math as m

print(m.e)
print(m.pi)
'''
#----------------------


'''
from math import pi
print(pi)
''' 


#importing example module here:

import example
# now we have access to everything in example module

result = example.pi
print(result)
result = example.square(3)
print(result)
result = example.cube(3)
print(result)
result = example.circumference(3)
print(result)
result = example.area(3)
print(result)
