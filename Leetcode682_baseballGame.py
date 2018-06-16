# Leetcode682_baseballGame.py

def calPoints(ops):
    ans = []
    for i in range(0, len(ops)):
        if ops[i] == 'C':
            ans.pop()
            # print(ans)
        elif ops[i] == 'D':
            ans.append(ans[-1] * 2)
            # print(ans)
        elif ops[i] == '+':
            ans.append(ans[-1] + int(ans[-2]))
            # print(ans)
        else:
            ans.append(int(ops[i]))
            # print(ans)
    return sum(ans)

print(calPoints(["5","2","C","D","+"]))
print(calPoints(["5","-2","4","C","D","9","+","+"]))
