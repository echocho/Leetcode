# Leetcode557_reverseWordsInString.py

def reverseWords(s):
    s = s.split()
    for i in range(0, len(s)):
        s[i] = s[i][::-1]
    s = ' '.join(s)    

    return s
print(reverseWords("Let's take LeetCode contest")=="s'teL ekat edoCteeL tsetnoc")