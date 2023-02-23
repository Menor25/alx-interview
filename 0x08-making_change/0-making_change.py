#!/usr/bin/python3
"""Defines the function makeChange."""


def makeChange(coins, total):
    """Returns fewest number of coins needed to meet total.
    Parameteres:
        - coins: a  list of values of coins in your possession
        - total: given amount to meet.
    """
    if total <= 0:
        return 0
    if len(coins) is 0:
        return -1
    coins = sorted(coins)
    dynamic = [float('inf')] * (total + 1)
    dynamic[0] = 0
    for i in range(total + 1):
        for coin in coins:
            if coin > i:
                break
            if dynamic[i - coin] != -1:
                dynamic[i] = min(dynamic[i - coin] + 1, dynamic[i])
    if dynamic[total] == float('inf'):
        return -1
    return dynamic[total]