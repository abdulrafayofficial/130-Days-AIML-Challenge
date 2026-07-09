#Python Exception Handling:

    # The try block lets you test a block of code for errors.
    # The except block lets you handle the error.
    # The else block lets you execute code when there is no error.
    # The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    # print(x)
# except NameError:
    print("An exception occured!")
except:
    print("something else is wrong")


# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised:
print('----------------------------------------------------')
print()

try:
    print("hello")
except:
    print('Something went Wrong!..')
else:
    print('Nothing went wrong')


#     Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
print('----------------------------------------------------')
print()
try:
    # print(y)
# except:
    print('Something went wrong dude!!...')
finally:
    print('The try except is finished!')


print('----------------------------------------------------')
print('Practical Example')

#Try to open a file that is not available:

try:
    f = open('demofile.txt')
    try:
        f.write('loremipsum')
    except:
        print('something went wrong when writing to the file.')
    finally:
        f.close()
except:
    print('Something went wrong when opening the file')

print('----------------------------------------------------')
print('Custom Exceptions:')
# a custom exception is a class that is derived from Python’s built-in Exception class.
class AgeError(Exception):
    "Raise Exception when the person is less than 18 years!..."
    pass
try:
    age = int(input("Enter your age: "))
    if age<18:
        raise AgeError
except AgeError:
    print('Person is not 18, and is not yet ready to vote!')
else:
    print("The person can vote")

