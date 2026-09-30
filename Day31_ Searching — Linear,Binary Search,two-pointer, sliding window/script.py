print("Hello World")
print('------------------------------------------------------')
print('Linear Search!')
lst = [5,8,4,6,9,2]
n = 8
pos = -1
def search(lst,n):
    global pos
    i = 0
    while i < len(lst):
        if lst[i] == n:
            pos = i
            return True
        i = i+ 1
    return False

if search(lst,n):
    print("Found!! at position: ",pos+1)
else:
    print("Not Found!! AHHHH")



#Approach using for loop instead of while loop

lst1 = [2,3,4,5,6,7]
num = 4
pos = -1
def linear_search(lst1,num):
    global pos
    for i in range(0 , len(lst1)):
        if lst1[i] == num:
            pos = i
            return True
    return False

if linear_search(lst1,num):
    print('AHHH Found at position: ',pos + 1)

else:
    print('NOOOO Not Found')




print('------------------------------------------------------')

print("Binary Search!..")

lst = [34, 12, 45, 87, 1, 43]
sorted_lst = sorted(lst)
n = 34

def binary_search(lst, n):
    l = 0
    u = len(lst) - 1

    while l <= u:
        mid = (l + u) // 2

        if lst[mid] == n:
            return mid
        elif lst[mid] < n:
            l = mid + 1
        else:
            u = mid - 1

    return -1

pos = binary_search(sorted_lst, n)
print(sorted_lst)
if pos != -1:
    print("Found at position:", pos + 1)
else:
    print("Not Found") 

        
print('------------------------------------------------------')


print('Two Pointers: ')

lst = [1, 3, 4, 6, 8, 11]
target = 10

def two_pointers(lst,target):
    left = 0
    right = len(lst) - 1

    while left < right:
        current = lst[left] + lst[right]

        if current == target:
            return (lst[left], lst[right])

        elif current < target: 
            left += 1

        else:
            right -=1

    return None

result = two_pointers(lst,target)
if result:
    print('Pair Found',result)
else:
    print('No Pair Found')

print('------------------------------------------------------')

print('Sliding Window')
lst = [2,1,5,1,3,2]
k = 3

def max_sum_subarray(lst,k):
    window_sum = sum(lst[:k])
    max_sum = window_sum

    for i in range(k , len(lst)):
        window_sum = window_sum + lst[i] - lst[i-k]
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum

print('Max Sum: ',max_sum_subarray(lst,k))