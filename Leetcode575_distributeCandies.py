# Leetcode575_distributeCandies.py

def distributeCandies(candies):
    '''
    :type candies: List[int]
    :rtype: int
    '''
    # original soution
    '''
    candies_set = set(candies)
    if len(candies_set) <= len(candies) /2:
        return len(candies_set)
    return int(len(candies)/2) '''

    # a more elegent solution:
    return min(int(len(candies)/2), len(set(candies)))

print(distributeCandies([1,1,2,3]))
print(distributeCandies([1,1,2,3,4,5]))
print(distributeCandies([1,1,2,3,4,5,5,3,2,5]))