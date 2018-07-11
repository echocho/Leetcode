# Leetcode463_islandPerimeter.py

def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # Solution 1: Firstly, calculate the number of grid in the island and the total perimeter providing all grids are isolated from one another.
    # Secondly, eliminate overlap borders.

    # O(rows_cnt * colums_cnt)

    total_perimeter = 0
    for rows in grid:
        total_perimeter += rows.count(1) * 4

    # search horizontally/ rows
    for row in grid:
        for i in range(len(row) - 1):
            if row[i] == row[i + 1] == 1:
                total_perimeter -= 2

    # search vertically/ columns
    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            if grid[i][j] == grid[i + 1][j] == 1:
                total_perimeter -= 2

    return total_perimeter
    
grid1= [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

grid2 = [
    [0,1,1,1],
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0]
]

grid3 = [[1],[0]]

print(islandPerimeter(grid1) == 16)
print(islandPerimeter(grid2) == 16)
print(islandPerimeter(grid3) == 4)
