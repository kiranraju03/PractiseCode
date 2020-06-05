"""
Find an element in a sorted square matrix

Logic : In summary, the idea of this great algorithm from Keith Schwartz [1] reduces one row or one column in each iteration.
        The runtime is only O(2n) instead of O(n^2) for a squared matrix with n rows and columns.
"""


def find_matrix(matrix, value):
    total_size = len(matrix)
    if total_size == 0:
        return False

    first_row_length = len(matrix[0])
    if first_row_length == 0:
        return False

    # Valid matrix, start searching
    i = 0
    j = first_row_length - 1
    while i < total_size and j >= 0:
        if matrix[i][j] == value:
            print("Found at : ["+str(i)+"]["+str(j)+"]")
            return True
        elif matrix[i][j] < value:
            i = i + 1
        else:
            j = j - 1
    return False


sorted_square_matrix = [[3, 4, 4, 6], [6, 8, 11, 12], [6, 8, 11, 15], [9, 11, 12, 17]]

print(find_matrix(sorted_square_matrix, 17))
