# Leetcode58_lengthofLastWord.py


def length_of_last_word(s):
    cnt = 0
    for c in s.strip():
        cnt += 1
        if c == ' ':
            cnt = 0
    return cnt


print(length_of_last_word('Hello World') == 5)
print(length_of_last_word('the Long and Winding Road') == 4)
print(length_of_last_word('helsfjkadf lajfkadjfl') == 10)
print(length_of_last_word('') == 0)
print(length_of_last_word('a') == 1)
