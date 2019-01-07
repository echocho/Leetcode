# use a dictionary to keep track of occurances of each word
def uncommonFromSentences(A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    wdict = {}
    words = A.split() + B.split()
    for i in words:
        wdict[i] = wdict.get(i, 0) + 1
    return [i for i in wdict.keys() if wdict[i] == 1]
print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(uncommonFromSentences("apple apple", "banana"))