# Leetcode832_flippingAnImage.py

def flipAndInvertImage(A):
    res = []
    for m in A:
        m = m[::-1]
        for n in range(len(m)):
            m[n] ^= 1
        res.append(m)
    return res
    
    
    
    
    # res = []
    # for i in range(len(A)):
    #     print('i= ', i)
    #     for k in A[i]:
    #         print('k= ', k)
    #         k ^= 1
    #         print('k^1= ', k)
    #     print('after xor i= ', i)
    #     res.append(i)
    # return res
print(flipAndInvertImage([[1,1,0], [1,0,1], [0,0,0]]))
print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))