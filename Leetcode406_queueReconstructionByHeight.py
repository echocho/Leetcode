# Leetcode406_queueReconstructionByHeight.py

def reconstructQueue(people):
    # Solution 1: first sort this list into an descending order base on their height
    # and then insert them in to the queue according to the number of people before them

    # O(n**2)

    people.sort(key = lambda (h, k): (-h, k))
    print('people', people)
    ans = []
    for p in people:
        ans.insert(p[1], p)
        print(ans)
    return ans

print(reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))

