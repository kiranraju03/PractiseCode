
elem_count = int(input())
arr = []

arr = list(map(int, input().split()))
print(arr)
sum_arr = sum(arr)
print(sum_arr)
arr.sort()
print(arr)
for each_elem in arr:
    bt_sum = each_elem * elem_count
    if bt_sum > sum_arr:
        print(each_elem)