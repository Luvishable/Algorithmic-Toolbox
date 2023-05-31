"""
Top Down with Memoization

- Solve the bigger problem by recursively finding the soolution to smaller subproblems. Whenever we solve a subproblem
we cache its result so that we don't end up solving it repeatedly if it's called multiple times. This tecnique
of storing the results of already solved subproblems is called MEMOIZATION.


Let's create a Fibonacci function with top down memoization approach
"""


def fibonacci_memo(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    # if the fibonacci(n) was not solved in the previous steps, then solve it and then cache it to the dictionary
    if not n in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    my_dict = {}
    print(fibonacci_memo(9, my_dict))
