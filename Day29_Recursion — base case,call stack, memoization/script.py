# Recursion:
    # A Function that calls itself within
    # helps to visualize a complex problem into basic steps
    # which can be solved more easily iteratively or recursively


# factorial(7) --> 7*6*5*4*3*2*1

# factorial(n) = n * fuctorial(n-1) --> formula

def factorial(n):
    # Base Case: stopping condition
    if(n==0 or n==1):
        return 1

    else:
        
        return n * factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))


#fibonacci sequence

def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))



#Iterative Approach

def walk(steps):
    for step in range(1,steps+1):
        print(f"You take step #{step}")

# walk(100)

#Recursive Approach

def walk2(steps):
    if steps == 0:
        return

    walk2(steps - 1)
    print(f"You take step #{steps}")



# walk2(50)



# Memoization:
import time
#unmemoized way:

# def slow_square(n):
#     time.sleep(2)
#     result = n ** 2
#     return result

# start = time.time()
# print(slow_square(2))
# print(slow_square(2))
# end = time.time()
# print(f"Time Taken: {round(end - start,2)} seconds")


#memoized way but messy:

square_cache = {}
def slow_square(n):
    if n in square_cache:
        return square_cache[n]
    time.sleep(2)
    result = n **2
    square_cache[n] = result
    return result

# start = time.time()
# print(slow_square(2))
# print(slow_square(2))
# end = time.time()
# print(f"Time Taken: {round(end - start,2)} seconds")
#this time it only took 2 seconds.... this means that this function is memoized


#correct way to memoize

from functools import lru_cache
@lru_cache
def sloww_square(n):
    result = n **2
    return result
start = time.time()
print(sloww_square(3))
print(sloww_square(3))
end = time.time()
print(f"{round(end-start,2)} seconds")

    

