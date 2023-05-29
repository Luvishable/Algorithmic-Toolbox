"""
Many children came to a celebration. Organize them into the minimum possible number of groups such that the age of any
two children in the same group differs by at most two years
"""

"""
Now, we can consider the ages as points in a line. What we want to do is to draw a length of 2 lines and try to cover 
the most lines as possible as. 
"""

""" 
We assume that the ages list is sorted. Let's consider a list like below:
[1, 1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 7, 8, 8, 9]
The groups will be (1-3), (4-6), (7-9) so totally 3.
"""


def celebration_party(ages):
    n = len(ages)

    # this array will hold the answer
    segments = []

    # we assume that our safe move is the leftmost element in the array as it is sorted.
    left = 0

    # starting the outer loop which will have borders the min and the max ages in a group
    while left <= n - 1:
        # initialing the l and r pointers. they are gonna dynamically create the borders
        l = ages[left]
        r = ages[left] + 2
        # append the group into answer array
        segments.append((l, r))
        left += 1
        # move the pointer l to the index which is greater than r(upper bound)
        while left <= n - 1 and ages[left] <= r:
            left += 1
    return segments


print(celebration_party([1, 1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 6, 7, 7, 7, 7, 8, 8, 9]))
