"""
2D Array pattern sum

In a 6*6 2D matrix array, find the sum of the elements in a specific pattern and find the max sum of them

2D Matrix :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

Pattern type :
1 1 1   1 1 0   etc
  1       0
1 1 1   1 1 0
"""

# board = []

# for i in range(6):
#     board.append([int(x) for x in input().split()])


def array_pattern_sum(board):

    i, j = 0, 0

    m = sum([board[i][j], board[i][j + 1], board[i][j + 2], board[i + 1][j + 1], board[i + 2][j], board[i + 2][j + 1],
             board[i + 2][j + 2]])

    for i in range(4):
        for j in range(4):
            acc = sum(
                [board[i][j], board[i][j + 1], board[i][j + 2], board[i + 1][j + 1], board[i + 2][j], board[i + 2][j + 1],
                 board[i + 2][j + 2]])
            m = max(m, acc)
    print(m)


array_pattern_1 = [[1, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]


array_pattern_2 = [[1, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0, 0],
                 [10, 2, 3, 5, 1, 0],
                 [0, 0, 0, 4, 0, 0],
                 [5, 6, 2, 6, 7, 0]]

array_pattern_sum(array_pattern_1)
array_pattern_sum(array_pattern_2)