"""
We can utilize divide and conquer paradigm in order to create binary search algorithm.

This algorithm compares the value to find and ignores the half of the elements after comparison. By doing so, the it
works fast.

We can create this algorithm in two ways: recursive and iterative

"""


# RECURSIVE WAY
# returns: index of x
def binary_search_rec(array, low, high, x):
    # base case
    if high >= low:
        middle = (high + low) // 2

        # if element is present at the middle itself
        if array[middle] == x:
            return middle

        # if element is smaller than middle, then it can only be present in the left subarray
        elif array[middle] > x:
            return binary_search_rec(array, low, middle - 1, x)

        # else the element can only be present in the right subarray
        else:
            return binary_search_rec(array, middle + 1, high, x)

    else:
        # element is not present in the array
        return -1


# ITERATIVE WAY
# returns: the index of x
def binary_search_iter(array, x):
    low = 0
    high = len(array) - 1
    middle = 0

    while low <= high:
        middle = (high + low) // 2

        # if x is greater, ignore the half
        if array[middle] > x:
            low = middle - 1

        # if x is smaller, ignore the half
        elif array[middle] < x:
            high = middle + 1

        # means x is in the middle
        else:
            return middle

    # if we reach here, then element is not present in the array
    return -1
