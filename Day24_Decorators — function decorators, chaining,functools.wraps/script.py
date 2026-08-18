import time
from functools import wraps

def timer_dec(base_fn):
    @wraps(base_fn)
    def enhanced_fn(*args,**kwargs):
        start_time = time.time()
        result = base_fn(*args,**kwargs)
        end_time = time.time()
        print(f"Task Time: {end_time - start_time} seconds ")
        return result
    return enhanced_fn
        
@timer_dec
def brew_tea(tea_color,sleep_time): 
    '''This function is used for making tea'''
    print('Brewing tea....')
    time.sleep(sleep_time)
    print(f"Tea Color is {tea_color}")
    print('tea is ready!')

@timer_dec
def make_matcha():
    print('Making Matcha....')
    time.sleep(1)
    print('Matcha is ready!')

brew_tea('green',1)
make_matcha()

print(brew_tea.__name__)
print(brew_tea.__doc__)