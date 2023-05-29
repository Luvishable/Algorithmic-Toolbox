"""
Activity Selection Problem

Explanation:
- Given n number of activities with their start and end times. We need to select the maximum number of activities that
can be performed by a single person, assuming that a person can only work on a single activity at a time.

Greedy Algorithm
- Sort activities based on their finish times
- Select first activity from sorted array
- For all remaining activites:
    if the start time of this activity is greater than or equal to the finish time of the previously selected activity
    then select this activity
"""


class Activity:
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish


def activity_selection(activities):
    answer = 0

    # sort the list according to the finish times
    activities.sort(key=lambda x: x.finish)

    # point the first activity as it has the earliest finish
    former = 0

    # traverse the list and if the former activity's finish time is smaller than
    # the latter activity's start time increase the answer
    for latter in range(1, len(activities)):
        if activities[latter].start > activities[former].finish:
            former = latter
            answer += 1
    # since the loop did not include the first activity, we manually add it
    return answer + 1


def main():
    activity1 = Activity("A1", 0, 6)
    activity2 = Activity("A2", 3, 4)
    activity3 = Activity("A3", 1, 2)
    activity4 = Activity("A4", 5, 8)
    activity5 = Activity("A5", 5, 7)
    activity6 = Activity("A6", 8, 9)
    activities = [activity6, activity5, activity4, activity3, activity2, activity1]
    return activity_selection(activities)


if __name__ == "__main__":
    print(main())
