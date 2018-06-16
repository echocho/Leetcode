# Leetcode821_shortestDistanceToAcharacter.py

def shortestToChar(S, C):
    key_pos = float('-inf')
    ans = []
    for num, char in enumerate(S):
        if char == C:
            key_pos = num
        ans.append(num - key_pos)
    
    key_pos = float('inf')
    for num in range(len(S)-1, -1, -1):
        if S[num] == C:
            key_pos = num
        ans[num] = min(ans[num], key_pos-num)
    
    return ans

        

print(shortestToChar('loveleetcode', 'e'))
