# Leetcode812_largestTriangleArea.py


def largestTriangleArea(points):
     """
    :type points: List[List[int]]
    :rtype: float
    """

     # Solution 1: Brute force. Use the shoelace formula to calculate the area
     # Check all possible combinations of unique coordinates and calculate each area.
     # Formula -- area = abs(x1 * y2 + x2 * y3 + x3 * y1 - x1 * y3 - x3 * y2 - x2 * y1) * 0.5
     # = abs(x1 * (y2 - y3)+ x2 * (y3 - y1)+ x3 * (y1 - y2)) * 0.5

     # O(n**3)

     max_area = 0
     length = len(points)

     for p1 in range(length - 2):
         for p2 in range(p1 + 1, length - 1):
             for p3 in range(p2 + 1, length):
                 x1, y1 = points[p1]
                 x2, y2 = points[p2]
                 x3, y3 = points[p3]

                 area = abs(x1 * (y2 - y3)
                            + x2 * (y3 - y1)
                            + x3 * (y1 - y2)) * 0.5

                 max_area = max(max_area, area)

     return max_area

print(largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]) == 2)

