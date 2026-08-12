# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Strings are also iterable objects, containing a sequence of characters:

mystr = 'Banana'
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

import random
class Dice:
    def __init__(self,rolls):
        self.rolls = rolls
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.rolls:
            self.count +=1
            return random.randint(1,6)
        else:
            raise StopIteration

# dice = Dice(3)
# for die in dice:
#     print(die)

dice = [die for die in Dice(4)]
print(dice)