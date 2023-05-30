"""
Merge Sort

- Merge Sort is a divide and conquer algorithm
- Divide the input array in two halves and we keep halving recursively until they become too small that cannot be broken
further
- Merge halves by sorting them

What we need in order to implement this algorithm is a function that merges two sorted lists. We gonna implement it first
"""


# utility function to merge two lists
def merge_two_sorted_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


# main function
def merge_sort(array):
    # whenever we have an array of size 1, we have to exit
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left, right)


# NOTE: Time Complexity of Merge Sort algorithm is: O(N log(N))
# NOTE: In merge sort all elements are copied into an auxiliary array. So N auxiliary space is required. O(N)

if __name__ == "__main__":
    array = [10, 3, 15, 7, 8, 23, 98, 29]
    print(merge_sort(array))
