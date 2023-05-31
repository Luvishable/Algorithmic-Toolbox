"""
                                    DYNAMIC PROGRAMMING

- DP is an algorithmic technique for solving an optimization problem by breaking it down into similar subproblems and
utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its
subproblems.

- If we compare DP and Divide&Conquer, we can see that DP is the optimization of D&C.

- DP has two main important features:

    1) Optimal Substructure: If any problem's overall optimal solution can be constructed from the optimal solutions of
    its subproblem then this problem has optimal substructure. D&C has this feature too.
    Example: Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)

    2) Overlapping Subproblem: Subproblems are smaller versions of the original problem. Any problem has overlapping
    sub-problems if finding its solution involves solving the same subproblem multiple times. This feature what makes
    DP different than D&C.


Let's consider Merge Sort algorithm: It has optimal substructure property because we repeatedly halve the array but it
has not overlapping subproblem because the halved arrays are independent of each other.
"""