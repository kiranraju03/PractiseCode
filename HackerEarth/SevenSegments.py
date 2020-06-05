tc = int(input())

seven_seg = {0: 6,
             1: 2,
             2: 5,
             3: 5,
             4: 4,
             5: 5,
             6: 6,
             7: 3,
             8: 7,
             9: 6}

for _ in range(tc):
    gen_code = ""
    numb = input()
    numb_seg_value = 0
    for n in numb:
        numb_seg_value += seven_seg[int(n)]

    if numb_seg_value % 2 == 0:
        one_segs = numb_seg_value // 2
        gen_code += '1' * one_segs
    elif numb_seg_value == 5:
        gen_code += '71'
    elif numb_seg_value == 3:
        gen_code += '7'
    elif numb_seg_value == 7:
        gen_code += '711'

    print(gen_code)

# Working

sticks = {"0": 6, "1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6}
N = int(input())
for _ in range(N):
    num = list(input())
    total = 0
    for i in num:
        total += sticks[i]
    if total % 2 == 0:
        print("1" * (total // 2))
    else:
        print("7" + "1" * (total // 2 - 1))
