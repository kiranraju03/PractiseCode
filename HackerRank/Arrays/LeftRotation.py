"""
Left/Right Rotation
Rotate array elements with the given number of rotation count

Complexity :
Time : O(N * C) : N is the size of the array, C is the count of rotations to be performed
Space : O(N) : Rearrange the elements of the array, worst case all
"""


def rotLeft(array, rotate_count):
    for each_rot in range(rotate_count):
        p = array.pop(0)
        array.append(p)
    return array


def rotRight(array, rotate_count):
    for each_rot in range(rotate_count):
        p = array.pop(-1)
        array.insert(0, p)
    return array


print(rotLeft([1, 2, 3, 4, 5], 2))
print(rotRight([1, 2, 3, 4, 5], 4))

