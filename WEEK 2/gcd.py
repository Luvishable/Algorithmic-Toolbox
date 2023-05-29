"Greatest Common Divisor algorithm"

# 1) In the first approach, choose the smaller number and initiate a loop from 1 to smaller + 1(include small)
# Then divide the two numbers by the current number in the loop. If both numbers are divided right, then update the gcd
def gcd_1(x, y):
    if x > y:
        small = y
    else:
        small = x
    gcd = 1
    for i in range(1, small + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd


# 2) Euclidian Algorithm
def gcd_2(x, y):
    while y:
        x = y
        y = x % y
    return abs(x)
