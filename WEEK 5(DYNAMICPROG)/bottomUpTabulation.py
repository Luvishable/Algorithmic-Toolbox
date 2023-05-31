"""
Bottom Up With Tabulation

- Tabulation is the opposite of the top-down memoization approach and avoids recursion.
- In this approach, we solve the problem bottom-up (by solving all the related subproblems first). This is done by
filling up a table. Based on the results in the table, the solution to the top/original problem is then computed.

Let's create a fibonacci function with this approach

"""


def fibonacci_tabulation(n):
    tabulation = [0, 1]
    for i in range(2, n + 1):
        tabulation.append(tabulation[i - 1] + tabulation[i - 2])
    return tabulation[n - 1]


if __name__ == "__main__":
    print(fibonacci_tabulation(9))
