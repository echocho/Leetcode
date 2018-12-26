# solution1: extra space
def sortArrayByParityII(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    evens, odds, output = [], [], []
    for i in A:
        if i % 2 == 0:
            evens.append(i)
        else: 
            odds.append(i)
    
    for i in range(len(evens)):
        output.append(evens[i])
        output.append(odds[i])
    return output

# print(sortArrayByParityII([4,7,2,5,6,9]))

# solution2: inplace - make each A[i%2==0] is even
def sortArrayByParityII(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    j = 1
    for i in range(0, len(A), 2):
        if A[i] % 2:
            while A[j] % 2:
                j += 2
            A[i], A[j] = A[j], A[i]
    return A
print(sortArrayByParityII([1,3,5,2,4,6]))    
print(sortArrayByParityII([4,7,2,5,6,9]))


