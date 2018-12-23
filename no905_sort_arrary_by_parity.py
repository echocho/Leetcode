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

#solution3: inplace; use quick sort algorithm
def sortArrayByParity(A):
    left, right = 0, len(A) -1 
    while left < right:
        if A[left] % 2 > A[right] % 2:
            A[left], A[right] = A[right], A[left]
        if A[left] % 2 == 0:
            left += 1
        if A[right] % 2 == 1:
            right -= 1
    return A
print(sortArrayByParity([3,1,2,4]))
print(sortArrayByParity([1]))
print(sortArrayByParity([1,0,3]))
print(sortArrayByParity([0,1,2]))