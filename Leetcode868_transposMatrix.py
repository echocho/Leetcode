# Leetcode868_transposMatrix.py

def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """

    # O(len_a * len_sub)

    if not A:
        return []

    len_a = len(A)
    len_sub = len(A[0])

    ans = [[0] * len_a for i in range(len_sub)]

    for i in range(len_sub):
        for j in range(len_a):
            ans[i][j] = A[j][i]

    return ans

print(transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
print(transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]])
