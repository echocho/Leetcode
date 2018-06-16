# Leetcode836_rectangleOverlap.py
def isRectangleOverlap(rect1, rect2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
    return rect2[0] < rect1[2] or rect2[1] < rect1[3] or  



print(isRectangleOverlap([0,0,2,2], [1,1,3,3]))
print(isRectangleOverlap([-2,1,-1,2], [-3,1.5,-1.5,3]))