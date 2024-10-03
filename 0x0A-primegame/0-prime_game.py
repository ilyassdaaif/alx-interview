#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): number of rounds
        nums (list): array of n
    Returns:
        str: name of winner (Maria or Ben) or None
        if winner cannot be determined
    """
    if not nums or x < 1:
        return None
    max_num = max(nums)

    # Generate primes up to max number using Sieve of Eratosthenes
    primes = [True for _ in range(max(max_num + 1, 2))]
    primes[0] = primes[1] = False

    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Count primes up to each number in nums
    prime_counts = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_counts[i] = prime_counts[i - 1]
        if primes[i]:
            prime_counts[i] += 1

    maria_wins = 0
    ben_wins = 0  # Initialize ben_wins
    for n in nums:
        if n < 2:
            ben_wins += 1
        elif prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins * 2 > x:
        return "Maria"
    elif maria_wins * 2 < x:
        return "Ben"
    return None
