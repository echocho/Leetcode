class Solution(object):
    def __init__(self):
        self.connected_components = set()

    def getComponentsInDirection(self, grid, coordinates, curr_color):
        for (x, y) in coordinates:
            if grid[x][y] != curr_color:
                return
            self.connected_components.add((x,y))

    def getConnectedComponents(self, grid, r0, c0, curr_color):
        up_cor = [(x, c0) for x in range(r0+1, -1, 1)]
        down_cor = [(x, c0) for x in range(r0+1, len(grid))]
        left_cor = [(r0, y) for y in range(c0-1, -1, -1)]
        right_cor = [(r0, y) for y in range(c0+1, len(grid[0]))]

        for coordinates in [up_cor, down_cor, left_cor, right_cor]:
            self.getComponentsInDirection(grid, coordinates, curr_color)

        for (x, y) in self.connected_components:
            self.getConnectedComponents(grid, x, y, curr_color)

    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        curr_color = grid[r0][c0]

        self.getConnectedComponents(grid, r0, c0, curr_color)

        for (x, y) in self.connected_components:
            grid[x][y] = color

        return grid


print(Solution().colorBorder(grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3))