"""
Jumping on clouds

find the number of jumps that can be made to move from one cloud to another by avoiding the thunder clouds represented
by 1 and jump only on normal clouds represented by 0. Max jumps can be either 1/2 places.
Return the number of jumps made.

I/P : An array of 0/1

Complexity :
Time : O(N) : N is the size of the array containing the clouds status
Space : O(1)
"""


def jumpClouds(cloudArr):
    no_of_jumps = 0
    current_pos = 0
    jumped_clouds = "0"

    while current_pos < len(cloudArr):
        # check for a normal cloud from the start to jump on, by 1/2 moves
        if (current_pos + 2 < len(cloudArr)) and (cloudArr[current_pos + 2] == 0):
            # we can make 2 moves and 1 jump
            no_of_jumps += 1
            current_pos += 2
            jc = " -> " + str(current_pos)
            jumped_clouds += jc

        elif (current_pos + 1 < len(cloudArr)) and (cloudArr[current_pos + 1] == 0):
            # we can make 1 moves and 1 jump
            no_of_jumps += 1
            current_pos += 1
            jc = " -> " + str(current_pos)
            jumped_clouds += jc

        else:
            # if not found, more one step ahead
            current_pos += 1

    print(no_of_jumps)
    print(jumped_clouds)


jumpClouds([1, 0, 1, 0, 0, 1, 0])
