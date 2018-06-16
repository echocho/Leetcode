# Leetcode771_jewelsAndStones.py
def numJewelsInStones(J, S):
    Jset = set()
    count = 0
    for i in J:
        Jset.add(i)
    for k in S:
        if k in Jset:
            count += 1
    return count
print(numJewelsInStones('aA', 'aAAbbb'))
