# leetcode_66_plus_one.py
def plusOne(digits):
    a = []
    b = []
    for i in digits:
        a.append(str(i))
    num = ''.join(a)
    num = int(num)
    plus = num + 1
    for k in str(plus):
        b.append(int(k))
    return b
print(plusOne([1,2,9]))

