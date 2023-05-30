"""
Quicksort Algorithm:

- Divide and Conquer approach is used
- Best case O(N * logN)
- Worst case O(N**2)
- Auxiliary Space: O(1)

- When the pivot is chosen poorly, it tends to worst case.
- Efficient on large datasets

"""


def swap(array, index1, index2):
    # easy way to swap in python
    array[index1], array[index2] = array[index2], array[index1]


def pivot(array, pivot_index, end_index):
    # firstly, we need end_index of the list as we wanna loop through the end of the list
    # in the beginning the 'swap_index' and 'pivot_index' points the same element which in our case is the first element
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if array[i] < array[pivot_index]:
            swap_index += 1
            swap(array, swap_index, i)
    # at the end of the loop, swap the pivot_index with swap_index
    # because the element at which pivot_index points have to be in the place where the swap_index points.
    swap(array, pivot_index, swap_index)
    return swap_index


def quicksort(array, left, right):
    if right > left:
        pivot_index = pivot(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)
    return array


if __name__ == "__main__":
    array = [
        3,
        5,
        0,
        6,
        2,
        1,
        4,
        23,
        12,
        76,
        34,
    ]
    left = 0
    right = len(array) - 1
    print(quicksort(array, 0, len(array) - 1))
