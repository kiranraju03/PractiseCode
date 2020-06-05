def bstArrStruct(arr):
    a = []
    for i in range(len(arr)):
        k = l = 1
        for j in range(len(a)):
            if arr[i] < a[j]:
                l = j
            else:
                k = j
        if k > 0:
            a.insert(k+2, arr[i])
        elif l > 0:
            a.insert(l, arr[i])
    print(a)

bstArrStruct([10,8,5])