#Task 01
import time
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n<=1:
        return n
    return fib(n - 1) + fib(n - 2)

start_time = time.time()
print(fib(35))
print(f"Time Taken: {time.time() - start_time} seconds")


#Task 02
from functools import partial
def multiply(a,b):
    return a*b

triple = partial(multiply,b=2)
print(triple(3))