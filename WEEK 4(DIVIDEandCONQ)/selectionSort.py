"""
- In case of selection sort, we repeatedly find the minimum element and move it to the sorted part of the array
to make unsorted part sorted.

- Selection sort performs well on small arrays.
"""


def selection_sort(array):
    # find the minimum element and swap it with the leftmost element
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp
    return array

# NOTE: Time Complexity of Selection Sort algorithm is O(N**2)


if __name__ == "__main__":
    array = [2, 1, 7, 6, 5, 3, 4, 9, 8]
    print(selection_sort(array))
