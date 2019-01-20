def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,1]]
    pascal = [[1], [1,1],]
    for i in range(2, numRows):
        # print('i', i)
        # print('pascal[i-1]', pascal[i-1])
        sum_of_previous = [pascal[i-1][j] + pascal[i-1][j-1] for j in range(1, len(pascal[i-1]))]
        # print('sum_of_previous', sum_of_previous)
        pascal.append([1] + sum_of_previous + [1])
        # print('pascal', pascal)
    return pascal

generate(6)