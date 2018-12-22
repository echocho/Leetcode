
def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    planted = 0
    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
            flowerbed[i] = 1
            planted += 1
    return planted >= n
print(canPlaceFlowers([1,0,0,0,1], 3)==False)
print(canPlaceFlowers([1,0,0,0,1], 1)==True)
print(canPlaceFlowers([0,0,1,0,1,0], 1)==True)
print(canPlaceFlowers([0,0,1,0,1,0], 2)==False)
print(canPlaceFlowers([0,1], 0)==True)
print(canPlaceFlowers([0,1], 1)==False)
print(canPlaceFlowers([1,0], 0)==True)
print(canPlaceFlowers([1,0], 2)==False)

