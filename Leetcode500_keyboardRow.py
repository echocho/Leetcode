# Leetcode500_keyboardRow.py

def findWords(words):
    # row1 = ['Q', 'q', 'W', 'w', 'E', 'e', 'R', 'r', 'T', 't', 'Y', 'y', 'U', 'u', 'I', 'i', 'O', 'o', 'P', 'p']
    # row2 = ['A', 'a', 'S', 's', 'D', 'd', 'F', 'f', 'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l']
    # row3 = ['Z', 'z', 'X', 'x', 'C', 'c', 'V,' 'v', 'B', 'b', 'N', 'n', 'M', 'm']
    # method 1
    row1 = 'qwertyuiop'
    row2 = 'asdfghjkl'
    row3 = 'zxcvbnm'
    ans = []
    for word in words:
        r1, r2, r3 = [], [], []
        for i in word:
            if row1.find(i.lower()) != -1:
                r1.append(1)
            elif row2.find(i.lower()) != -1:
                r2.append(1)
            elif row3.find(i.lower()) != -1:
                r3.append(1)
        if len(r1) == len(word) or len(r2) == len(word) or len(r3) == len(word):
            ans.append(word)
    return ans
    

print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(findWords(["qz","wq","asdddafadsfa","adfadfadfdassfawde"]))
print(findWords(['qz']))
        
            
