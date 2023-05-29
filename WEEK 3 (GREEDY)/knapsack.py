"""
A burglar has broken into the house of a merchant of different spices and he wants to take as much value with him as
he can, but he only has a small knapsack which has capacity of only 15kg.

The formal definiton of the Fractional Knapsack:

Input: Weights w_1, ... , w_n and values v_1, ... , v_n of n items; capacity W.

Output: The maximum total value of fractions of items that fit into a knapsack of capacity W.

Lemma:
- There exists an optimal solution that uses as much as possible of an item with the maximal value per unit of weight

Greedy Algorithm:
- Calculate the density or ratio for each item
- Sort items based on this ratio
- Take items with the highest ratio sequentially until weight allows
- Add the next item as much (fractional) as we can

"""


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsack_method(items, capacity):
    # sort the items in descending order according to the ratio property
    items.sort(key=lambda x: x.ratio, reverse=True)

    used_capacity = 0
    total_value = 0

    for i in items:
        if used_capacity + i.weight <= capacity:
            used_capacity += i.weight
            total_value += i.value
        else:
            unused_weight = capacity - used_capacity
            used_capacity += unused_weight
            value = i.ratio * unused_weight
            total_value += value
        if used_capacity == capacity:
            break

    return total_value


def main():
    item1 = Item(20, 100)
    item2 = Item(30, 120)
    item3 = Item(10, 60)
    items_list = [item1, item2, item3]
    capacity = 50
    total_value = knapsack_method(items_list, capacity)
    return total_value


if __name__ == "__main__":
    print(main())
