#Generators:
            #Python generators are special functions that return a lazy iterator object,
            #  allowing you to produce a sequence of values over time on-demand 
            # instead of computing them all at once and saving them in memory


#The yield keyword is what makes a function a generator.
#When yield is encountered, the function's state is saved, and the value is returned.
#  The next time the generator is called, it continues from where it left off.
#Generators Saves Memory
'''
def topTen():
    yield 1
    yield 2
    yield 3
    yield 4
#we can yeild multiple values but can return only one!
values = topTen()
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())

'''
'''
def topTenSquares():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1
values = topTenSquares()
for i in values:
    print(i)

'''


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

# Generator Expressions:

# Similar to list comprehensions,
# you can create generators using generator expressions with parentheses instead of square brackets:

list_comp = [x for x in range(1,11)]
print(list_comp)

gen_exp = (x for x in range(1,11))
print(gen_exp)
print(list(gen_exp))

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

#yeild From Concept:

def old_way():
    for x in [1,2,3]:
        print(x)

old_way()

def new_way():
    yield from [1,2,3]

value = new_way()
print(next(value))
print(next(value))
print(next(value))


def gen_User_Id():
    count = 1

    while True:
        yield f"User: {count:.2f}"
        count +=1

user_gen = gen_User_Id()
print(user_gen.__next__())
print(user_gen.__next__())
print(user_gen.__next__())