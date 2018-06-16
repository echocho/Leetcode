# Leetcode492_ConstructRectangle.py
import math

def constructRectangle(area):
    '''type area: int
       rtype: List[int] '''
    
    width = int(math.sqrt(area))
    while area % width != 0:
        width -= 1
    return [int(area/width), int(width)]
        
    

print(constructRectangle(1))
print(constructRectangle(4))
print(constructRectangle(8))
print(constructRectangle(36))
print(constructRectangle(100))
print(constructRectangle(11))
