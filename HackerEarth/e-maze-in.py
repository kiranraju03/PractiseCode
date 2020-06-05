"""
Maze display

A person is stuck in a maze at a starting position of (0,0), a route map is given as an input, find the end position
after he has traversed the route map
Route Map directions, L,R,U,D : left, right, up and down

Hint : Numberical Scale concept

Complexity:
Time : O(N) : N is the length of the route map
Space : O(1)
"""

# Eg : LLRRDDUUDDLR
route_direction = input("Enter the route directions : ")

# initial position
x = y = 0

for each_direction in route_direction:
    if each_direction == "L":
        x -= 1
    elif each_direction == "R":
        x += 1
    elif each_direction == "U":
        y += 1
    elif each_direction == "D":
        y -= 1

print("%d %d" % (x, y))
