"""
Find the number of valleys covered by the traveller

'U' being the Uphill and 'D' being the downhill and the traveller has to return to sea level
Valley : Covering the downhill and reaching back the sea_level
Mount : Covering the uphill and reaching back to sea_level

Assumptions made : add 1 to sea_level when the traveller goes U and reduce it by 1 when he goes D and while adding
                    the U part, if he reaches the sea_level, he has covered a valley.
"""

def countingValleys(n, s):
    sea_level = valley = mount = 0
    for i in range(n):
        if (s[i] == 'U'):
            sea_level += 1
            if (sea_level == 0):
                valley += 1
        else:
            sea_level -= 1
            if (sea_level == 0):
                mount += 1
    print("Mountains covered :"+str(mount))

    return valley

#print(countingValleys(8,'UDDDUDUU'))
print(countingValleys(10,'DDUUUUDDDU'))