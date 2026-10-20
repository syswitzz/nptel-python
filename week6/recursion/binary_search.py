def binary_search(items, target):
    low = 0
    high = len(items)-1

    while low<=high:
        mid = int(low + (high-low)/2)

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# recursive version
def bs_recursive(items, target, low, high):
    # base case - only one element
    if low == high:
        if items[low] == target:
            return low
        else:
            return -1

    else:
        mid = int(low + (high-low)/2)

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            # right half
            return bs_recursive(items, target, low=mid+1, high=high)
        else:
            # left half
            return bs_recursive(items, target, low=low, high=mid-1)


 
print(bs_recursive([3,23,32,44,53,56,64,73], 72, 0, 7))