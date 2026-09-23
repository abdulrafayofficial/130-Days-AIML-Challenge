print('Sorting Algorithms')

# Sorting: Sorting is basically the process of arranging our data in a particular order


# Bubble Sorting:
arr = [5, 2, 8, 1, 9]
def bubble_sort(n):
    n = len(arr) #5
    for p in range(0,n-1): #0-4
        for i in range(0,n-p-1):
            if arr[i]> arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
    return arr
            
print(bubble_sort(arr))


#----------------------------------------------------------

#Selection Sorting

def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr


print(selection_sort(arr))


#----------------------------------------------------------

#Insertion Sorting

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

print(f'Insertion sorting: {insertion_sort(arr)}')



#----------------------------------------------------------

#Merge Sorting

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0
    while i<len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1

        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(f"Merge sorting: {merge_sort(arr)}")



#----------------------------------------------------------

#Quick Sorting


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle +quick_sort(right)


print(f"Quick Sorting: {quick_sort(arr)}")