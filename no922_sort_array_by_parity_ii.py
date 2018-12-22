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

print(sortArrayByParityII([4,7,2,5,6,9]))