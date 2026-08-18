#Loger Function Task!

from functools import wraps

def logger(base_fn):
    @wraps(base_fn)
    def enhanced_fn(*args,**kwargs):
        print(f"Calling {base_fn.__name__} with args: {args}, kwargs: {kwargs}")
        print("AHHHH")
        result = base_fn(*args,**kwargs)
        return result
    return enhanced_fn

@logger
def add(a,b):
    return a+b

print(add(4,5))


#@retry(n) Task!
def retry(n):
    def decorator(base_fn):
        @wraps(base_fn)
        def wrapper(*args,**kwargs):
            for attempt in range(n):
                try:
                    result = base_fn(*args,**kwargs)
                    return result
                except Exception:
                     print('Attempt Failed!')
            raise Exception(f"All {n} attempts failed!")

        return wrapper

    return decorator
