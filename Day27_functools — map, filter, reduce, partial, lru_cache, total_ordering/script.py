def cube(x):
    return x*x*x

print(cube(4))

lst = [1,2,3,4,5,6]
new_lst = []

for item in lst:
    cube_ = item*item*item
    new_lst.append(cube_)
print(new_lst)

#same thing is easier using map function

lst_new = list(map(cube,lst))
print(lst_new)

#Another example using lambda function:

n = [1,2,3]
result = list(map((lambda x:x*x*x),n))
print(result)

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#Filter Function:


def filter_function(a):
    return a>3

newnewlist = list(filter(filter_function,lst))
print(newnewlist)



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Reduce Function

from functools import reduce

numbers = [1,2,3,4,5]
def mySum(x,y):
    return x+y
sum = reduce(mySum,numbers)
print(sum)


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Partial function
from functools import partial
#regular function
def num_to_power(num,power):
    return num**power

# print(num_to_power(2,3))


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#partial function

square_it = partial(num_to_power,power= 2)
make_it_square = partial(num_to_power,10,2)#we can also do it this way!
print(square_it(3))
print(make_it_square())



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#lru_cache function
from functools import lru_cache
import time

@lru_cache(maxsize=None)
def heavy_Processing(n):
    time.sleep(2)
    return n*10

print(heavy_Processing(5))
print(heavy_Processing(5))



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#total ordering

from functools import total_ordering
@total_ordering
class Student:
    def __init__(self,gpa):
        self.gpa = gpa

    def __eq__(self, value):
        return self.gpa == value.gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

s1 = Student(2.3)
s2 = Student(3.8)
print(s1>s2)



