# 1) Recursive way
# Time complexity: O(2 ^ n)  Exponential, Auxiliary Space: O(n)
def fibonacci_1(n):
    if n < 0:
        return
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_1(n - 1) + fibonacci_1(n - 2)


# 2) Dynamic programming approach and space optimized
def fibonacci_2(n):
    a = 0
    b = 1

    if n < 0:
        return

    elif n == 0:
        return 0

    elif n == 1:
        return b

    # in else case, create a temp c variable in every loop that is the sum of a and b
    # assign a to the b, b to the c.
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
