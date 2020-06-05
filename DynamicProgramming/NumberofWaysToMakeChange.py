"""
FInd the number of ways the change(denoms) can be used to get a given amount
"""


def numberofDenoms(amount, denoms):
    # Creating an array of 0's representing the ways of using the denoms
    noOfWays = [0 for i in range(amount+1)]
    # for getting 0 amount, there is just one way, do nothing, so 1
    noOfWays[0] = 1
    for denom in denoms:
        for eachAmount in range(1, amount+1):
            if denom <= eachAmount:
                noOfWays[eachAmount] += noOfWays[eachAmount - denom]

    return noOfWays[amount]


print(numberofDenoms(6, [1, 5]))

