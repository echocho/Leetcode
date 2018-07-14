def floodFill(image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """
    # Solution 1: use deepth-first search. starting from (sr, sc), check if its four neighbors are of the same color.
    # if yes, change them to new color and check each individual's neighbor recursively.

    # O(N), N = amount of pixel in image

    color = image[sr][sc]
    row, column = len(image), len(image[0])
    if color == newColor:
        return image

    def dfs(r, c):
        if image[r][c] == color:
            image[r][c] = newColor
            if r >= 1:
                dfs(r-1, c)
            if r + 1 < row:
                dfs(r + 1, c)
            if c >= 1:
                dfs(r, c - 1)
            if c + 1 < column:
                dfs(r, c + 1)
    dfs(sr, sc)
    return image


image1 = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1; sc = 1; newColor = 2
print(floodFill(image1, sr, sc, newColor))


