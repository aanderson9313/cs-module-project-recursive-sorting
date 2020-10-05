# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start > end:
        return -1
    middle = (start + end)
    
    if target == arr[middle]:
        return middle
    else:
        if target < arr[middle]:
            end = middle - 1
        else:
            start = middle + 1
        return binary_search(arr, target, start, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
