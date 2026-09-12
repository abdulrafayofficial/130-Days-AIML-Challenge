from functools import lru_cache
import time
@lru_cache
def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
start  = time.time()
# print(fibonacci(40))
# print(fibonacci(40))
end = time.time()
# print(f"Total time : {round(end - start,2)} seconds")


#Tower Of Hanoi Problem....
def TOH(no_of_disks,start,aux,end):
    if no_of_disks == 1:
        print('Move disk 1 from rod {} to rod {}.'.format(start,end))
        return
    TOH(no_of_disks - 1,start,end,aux)
    print("Move disk {} from rod {} to rod {}".format(no_of_disks,start,end))
    TOH(no_of_disks - 1,aux,start,end)
disc = 3
# TOH(disc,'A','B','C')



nested_list = [1, [2, 3, [4, 5, [6, 7]]], 8]
def flatter(nested_list):
    lst = []
    for item in nested_list:
        if isinstance(item,list):
            flat = flatter(item)
            lst.extend(flat)
        else: 
            lst.append(item)

    return lst
print(flatter(nested_list))