"""
House Robber Problem

-Given N number of houses along the street with some amount of money
-Adjacent houses cannot be stolen
-Find the maximum amount that can be stolen

"""


# top-down memoization approach
def house_robber_TD(houses, current_index, dictionary):
    if current_index >= len(houses):
        return 0
    else:
        if current_index not in dictionary:
            steal_first_house = houses[current_index] + house_robber_TD(
                houses, current_index + 2, dictionary
            )
            skip_first_house = house_robber_TD(houses, current_index + 1, dictionary)
            dictionary[current_index] = max(steal_first_house, skip_first_house)
        return dictionary[current_index]


# bottom-up tabulation approach
def house_robber_BU(houses, current_index):
    temp_array = [0] * (len(houses) + 2)
    for i in range(len(houses), -1, -1):
        temp_array[i] = max(houses[i] + temp_array[i + 2], temp_array[i + 1])
    return temp_array[0]
