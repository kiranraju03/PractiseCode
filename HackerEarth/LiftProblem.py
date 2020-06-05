"""
In a building with 2 lifts, find which lift has to reach the requesting floor.
Both lifts are in the opposite directions, assuming the top floor to be 7th

print the lift that will reach the requesting floor

Complexity:
Time : O(1)
Space : O(1)
"""

test_Cases = int(input())

lift_a = 0  # ground floor
lift_b = 25  # top floor

for _ in range(test_Cases):
    requesting_floor = int(input())
    # If the floor is near B lift
    if abs(requesting_floor - lift_a) > abs(requesting_floor - lift_b):
        print('B')
        lift_b = requesting_floor
    elif abs(requesting_floor - lift_a) < abs(requesting_floor - lift_b):
        print('A')
        lift_a = requesting_floor
    elif abs(requesting_floor - lift_a) == abs(requesting_floor - lift_b):
        print('A')
        lift_a = requesting_floor
