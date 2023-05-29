"""
Problem:
n patients have come to the doctor's office at 9.00AM. They can be treated in any order. For i-th patient, the time
needed for treatment is t_i. You need to arrange the patients in such a queue that the total waiting time is minimized.
The output should be the minimum total waiting time

Greedy Algorithm:
1- First treat the patient with the minimum treatment time
2- Remove this patient from the queue
3- Treat all the remaining patients in such an order as to minimize their total waiting time
"""

"""
Subproblem: It is a similar problem of smaller size.  

Safe Choice: A greedy choice is called safe choice if there is an optimal solution consistent with this first choice. For 
example, to treat the patient with minimum treatment time (t_min) first is a safe choice.
"""


def patientQueue(times):
    n = len(times)
