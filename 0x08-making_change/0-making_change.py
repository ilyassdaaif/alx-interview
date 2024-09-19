#!/usr/bin/python3
"""
Module for making change using dynamic programming
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

    # Initialize dp array with total + 1 (impossible value)
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Iterate through all amounts from 1 to total
    for i in range(1, total + 1):
        # Try each coin
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
