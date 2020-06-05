"""
Counting Valley

Check for number of valleys crossed in a hike with uphills(U) and downhills(D)
When the hiker comes to a valley after U/D count the valley

Sample Input : UDDDUDUU

Visual : _ is the valley
_/\       _
   \    /
    \/\/

"""


def valleyCounter(path):
    sea_level = 0 # represents surface/valley
    valley = 0
    for each_part in path:
        # print(each_part)
        if each_part == "U":
            sea_level += 1
            if sea_level == 0:
                valley += 1
        else:
            sea_level -= 1

    return valley


print(valleyCounter("UDDDUDUU"))
print(valleyCounter("DDDUUDUDUUUUDDDU"))
