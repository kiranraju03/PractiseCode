"""
Sevens(Its-Magic)
Find the index of an element which only can be removed from the array, on doing so, the sum of the remaining elements
have to be divisible by 7. The index returned has to be the smallest element

Complexity:
Time : O(N) : N is the size of the array
Space : O(N-1) : Might be all elements can be divisible by 7 in the end_arr
"""

ints = int(input("Number of elements : "))

int_arr = list(map(int, input("Elements : ").split()))[:ints]
total_sum = sum(int_arr)

end_arr = []

for i in range(ints):
    # remove element and check if others are divisible by 7
    if (total_sum - int_arr[i]) % 7 == 0:
        end_arr.append(int_arr[i])

# If not found any, return -1
if len(end_arr) == 0:
    print('-1')

# If elements found, find the min and print the index of that element in the main array
else:
    min_ele = min(end_arr)
    req_pos = int_arr.index(min_ele)
    print(req_pos)
