# Leetcode766_ToeplitzMatrix.py

def is_toeplitz_matrix(matrix):
    # Solution 1: use the fact that (x1, y1) and (x2, y2) are diagonal if and only if (x1-y1) == (x2-y2)
    # O(rows * columns)

    d = {}

    for row_indx, row in enumerate(matrix):
        for column_indx, val in enumerate(matrix[row_indx]):
            if (row_indx - column_indx) not in d:
                d[row_indx - column_indx] = val
            else:
                if d[row_indx - column_indx] != val:
                    return False
    return True


matrix_1 = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]

matrix_2 = [
  [1,2],
  [2,2]
]

print(is_toeplitz_matrix(matrix_1) == True)
print(is_toeplitz_matrix(matrix_2) == False)



