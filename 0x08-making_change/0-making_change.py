#!/usr/bin/python3
"""
Module for making change using a greedy algorithm
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total

    Args:
    coins (list of int): list of coin denominations
    total (int): target amount

    Returns:
    int: fewest number of coins needed to meet total, -1 if not possible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    coin_count = 0
    for coin in coins:
        if total >= coin:
            # Use as many of this coin as possible
            coin_count += total // coin
            total = total % coin

        if total == 0:
            return coin_count

    return -1
