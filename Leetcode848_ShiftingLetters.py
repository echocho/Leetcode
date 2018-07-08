# Leetcode848_ShiftingLetters.py

def shiftingLetters(S, shifts):
    """
    :type S: str
    :type shifts: List[int]
    :rtype: str
    """
    all_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    seq = 1
    d = {}
    indx = []

    for letter in all_alphabets:
        d[letter] = seq
        seq += 1

    for char in S:
        indx.append(d[char])

    for i in range(len(indx)):
        indx[i] = indx[i] + sum([k for k in shifts[i:]])

    for j in indx:
        if j > 26:
            j %= 26

    return ''.join(m for m in [d.keys()[d.values().index(j)] for j in indx])


print(shiftingLetters('abc', [3,5,9]))
