fib_array = [0, 1]

length_of_fib_values = 10

# loop runs to 0 - 'n-2' as already 2 elements are added to the list
[fib_array.append(fib_array[-1] + fib_array[-2]) for i in range(length_of_fib_values - 2)]

print(fib_array)

"""
Memoized technique
"""
memoized = {}
def fib_m(x):
    if x in [0,1]:
        return 1
    elif x in memoized:
        return memoized[x]

    res = fib_m(x-1) + fib_m(x-2)
    memoized[x] = res
    return res

fib_m(20)
print(memoized)