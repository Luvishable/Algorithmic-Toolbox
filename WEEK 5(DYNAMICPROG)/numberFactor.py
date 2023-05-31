"""
As said earlier, dynamic programming is the optimization onto the divide&conquer algorithm. So the problems that can be
solved divide&conquer can be solved dynamic programming too.

Number Factor Problem:

- Given N, find the number of ways to express N as sum of 1,3,4.
- N=4 / Number of ways: 6 / {4},{1,3},{3,1},{1,1,1,1}

"""


# Top-Down Memoization Approach
def number_factor_TD(n, dictionary):
    # dp is the dictionary
    if n in (0, 1, 2):
        return 1
    if n == 3:
        return 2
    else:
        if n not in dictionary:
            rec1 = number_factor_TD(n - 1, dictionary)
            rec2 = number_factor_TD(n - 3, dictionary)
            rec3 = number_factor_TD(n - 4, dictionary)
            dictionary[n] = rec1 + rec2 + rec3
        return dictionary[n]


# Bottom-Up Tabulation Approach
def number_factor_BU(n):
    temp_array = [1, 1, 1, 2]
    for i in range(4, n + 1):
        temp_array.append(temp_array[i - 1] + temp_array[i - 3] + temp_array[i - 4])
    return temp_array[n]


# The reason why we created temp_array is that if n == 1 it can be created in one way which is {1} itself.
# For n == 2, we can create it with one way as well which is {1,1}. For n == 3, there are two ways {1,1,1},{3}
