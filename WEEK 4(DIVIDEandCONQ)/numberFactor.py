"""
Number Factor Problem

Explanation:
- Given N, find the number of ways to express N as sum of 1, 3 and 4.

Example 1:
- N = 4
- Number of ways: 4
- There are four ways we can express N => {4}, {1,3}, {3,1}, {1,1,1,1}


Example 2:
- N = 5
- Number of ways: 6
- There are 6 ways we can express N => {4,1}, {1,4}, {1,3,1}, {3,1,1}, {1,1,3}, {1,1,1,1,1}

-Let's divide the problem into subproblems. In order to get f(5) we need f(4) + 1. We already know f(4).
Then:
f(5) = f(4) + 1  or
f(5) = f(2) + 3 or
f(5) = f(1) + 4

"""


def number_factor(n):
    # base condition
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        subproblem_1 = number_factor(n - 1)
        subproblem_2 = number_factor(n - 3)
        subproblem_3 = number_factor(n - 4)
        return subproblem_1 + subproblem_2 + subproblem_3
