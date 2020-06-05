"""
Find the min number of coins required to form a given change
"""


def minNumofCoins(amount, denoms):
    numOfCoins = [float("inf") for i in range(amount + 1)]
    numOfCoins[0] = 0
    for denom in denoms:
        for eachAmount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[eachAmount] = min(numOfCoins[eachAmount], 1 + numOfCoins[eachAmount - denom])

    return numOfCoins[amount] if numOfCoins[amount] != float("inf") else -1


print(minNumofCoins(6, [1, 3, 4, 2]))