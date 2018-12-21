#solution 1: use additional lists to store even and odd nums respectively
def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    if not A:
        return []
    evens, odds = [], []
    for i in A:
        if i%2 > 0:
            odds.append(i)
        else:
            evens.append(i)
    return evens + odds

#solution 2: sort A by the remainer from x/2
def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    A.sort(key=lambda x: x%2)
    return A
