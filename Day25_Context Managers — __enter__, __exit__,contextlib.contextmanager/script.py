#Context managers allow you to allocate and release resources precisely when you want to...

import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        difference = self.end_time  - self.start_time
        print(f'The difference is {difference:.2f} seconds')


with Timer():
    time.sleep(1)


#Context Managers using Decorators

from contextlib import contextmanager
config = {"mode":"production"}

@contextmanager
def temp_setting(new_mode):
    old_mode = config['mode']
    config['mode'] = new_mode
    
    try:
        yield config
    
    finally:
        config['mode'] = old_mode

print(f'Before mode:  {config["mode"]}')
with temp_setting('Testing'):
        print(f'Inside Mode: {config["mode"]}')
    
print(f'After mode: {config["mode"]}')


