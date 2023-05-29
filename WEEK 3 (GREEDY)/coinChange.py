"""
Coin Change Problem

Explanation:
You are given coins of different denominations and total amount of money. Find the minimum number of coins that you need
to make up the given amount
"""


def coin_change(total_number, coins):
    # consider the total_number as the money that we want to change
    N = total_number

    # assign a variable to keep track how many coins we will have
    total_coins = 0

    # sort the coins list
    coins.sort()

    # keep track of the biggest coin's index
    # as we keep doing (N - biggest_coin).
    # We do not want this to be lower than 0
    index = len(coins) - 1

    while N > 0:
        current_coin_value = coins[index]
        if N >= current_coin_value:
            N -= current_coin_value
            total_coins += 1
            print(current_coin_value)

        if N < current_coin_value:
            index -= 1

    return total_coins


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100]
    money = 201
    print(coin_change(money, coins))
