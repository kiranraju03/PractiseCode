"""
Split Houses
"""

grids = int(input())

layout = input()

# flag = False

layout = layout.replace(".", "B")

# for j in range(grids - 1):
#     if layout[j] == "H" and layout[j + 1] == "H":
#         print("NO")

if 'HH' in layout:
    print('NO')
else:
    print("YES\n" + layout)