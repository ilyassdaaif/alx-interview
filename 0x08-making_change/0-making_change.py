#!/usr/bin/python3
"""
Determine the fewest number of coins needed to meet a given amount total
"""
total1 = 37
list_of_coins1 = [1, 2, 25]

#total2 = 1453
#list_of_coins2 = [1256, 54, 48, 16, 102]

def makeChange(coins, total):
    if total <= 0:
        return 0

    remainder = total  # 37

    coins_needed = 0

    coin_index = 0

    sorted_coins_list = sorted(coins, reverse=True)
    # [25, 2, 1]

    list_len = len(coins)  # 3

    while remainder > 0:  # 0

        if coin_index >= list_len:  # index 1 < 3
            return -1

        if remainder - sorted_coins_list[coin_index] >= 0:  # 2 - 2 = 0
            remainder -= sorted_coins_list[coin_index]  # 0

            coins_needed += 1  # 1
        else:
            coin_index += 1
    return coins_needed  # 7
