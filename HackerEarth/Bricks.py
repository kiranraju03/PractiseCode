"""
Find the person who moved the last brick

given the total bricks, first person picks i brick, then the second person picks i*2 bricks
print the person who places the last brick

Complexity :
Time : O(N) :  N is the number of bricks
Space : O(1)
"""

bricks_count = int(input())

for i in range(bricks_count):
    print(i)
    # First person picks i bricks, check if he placed the last
    bricks_count -= i
    if bricks_count <= 0:
        print("First")
        break
    # Second person placed i*2 bricks, check if he emptied the bricks
    bricks_count -= i * 2
    if bricks_count <= 0:
        print("Second")
        break

# My complex answer :
# def brick_placer(brick_count):
#     p = m = 0
#     t = 0
#     diff = brick_count
#     for i in range(1, (int( brick_count/3 )) + 1 ):
#         if t < diff:
#             p = i
#             m = i * 2
#             t += (p + m)
#             diff = brick_count - t
#         elif i > diff:
#             return "First"
#         else:
#             return "Second"

# print(brick_placer(brick_count))