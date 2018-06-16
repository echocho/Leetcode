# Leetcode406_queueReconstructionByHeight.py
import heapq
def reconstructQueue(people):
    # method 1
    people.sort(key = lambda (h, k): (-h, k))   # O(nlogn)
    ans = []
    for p in people:                            # O(n**2)
        ans.insert(p[1], p)
    return ans

print(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))

