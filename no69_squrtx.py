# use binary search
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 2:
        return x
    
    left, right, = 1, x
    pivot = left + len(range(left, right)) // 2
    while left < pivot and right > pivot:
        if pivot ** 2 == x:
            return pivot
        if pivot ** 2 > x:
            right = pivot 
        elif pivot ** 2 < x:
            left = pivot 
        pivot = left + len(range(left, right)) // 2 
    if right >= pivot:
        return left
    return right
        
print(mySqrt(200))


# what looks a bit simpler
def solution():
    if x < 2:
        return x
    
    left, right, = 1, x
    while left < right:
        m = left + (right - left) // 2
        if m <= x / m:
            left += 1
        else: 
            right = m
    return m
        