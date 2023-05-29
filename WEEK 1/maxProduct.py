"""
Find a pair with maximum product in array of Integers.

Given an array with both positive and negative integers, return a pair with the highest product.
"""


# 1) The most unoptimized solution would be the following function.
# Time Complexity: O(n2), Auxiliary Space: O(1)
def maxProduct_1(array):
    n = len(array)
    if n < 2:
        return

    a = array[0]
    b = array[1]

    # Traversing every possible pair and keep track of the max product
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] * array[j] > a * b:
                a = array[i]
                b = array[j]
    return [a, b]


# 2) A better solution would be to sort the array in increasing order. If all the elements are positive return the
# product of last two elements. Else multiply first two elements and last two elements; return the one greater.
# Time Complexity: O(nlog n), Auxiliary Space: O(1)
def maxProduct_2(array):
    array.sort()
    num1 = 0
    num2 = 0

    # length of array
    n = len(array)

    # calculate the product of the two smallest number
    two_smallest = array[0] * array[1]

    # calculate the product of the two largest number
    two_largest = array[n - 1] * array[n - 2]

    if two_largest > two_smallest:
        return [array[n - 2], array[n - 1]]
    else:
        return [array[1], array[0]]


# For more efficient solution, traverse the array in one loop and keep track of the following four properties:
# max positive value, second max positive value, min negative second min negative value its absolute value
# Time complexity: O(n), Auxiliary Space: O(1)
def maxProduct_3(array):
    n = len(array)
    if n < 2:
        return
    if n == 2:
        return array

    # initialize the max and second max value
    max_a = 0
    max_b = 0

    # initialize the min and second min
    min_a = 0
    min_b = 0

    for i in range(n):
        # update max and second max if so
        if array[i] > max_a:
            max_b = max_a
            max_a = array[i]
        elif array[i] > max_b:
            max_b = array[i]

        if min_a > array[i]:
            min_b = min_a
            min_a = array[i]

        elif min_b > array[i]:
            min_b = array[i]

    two_largest = max_a * max_b
    two_smallest = min_a * min_b

    if two_largest > two_smallest:
        return [max_a, max_b]
    else:
        return [min_a, min_b]
