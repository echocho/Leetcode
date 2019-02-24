import re

class Solution:
    def myAtoi(self, strs: str) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        pattern = '(^[\+\-0]*\d+)'
        target = re.findall(pattern, strs.lstrip())
        try:
            res = int(''.join(target))
            if res > MAX_INT:
                return MAX_INT
            elif res < MIN_INT:
                return MIN_INT
            else:
                return res
        except:
            return 0

print(Solution().myAtoi("42")==42)
print(Solution().myAtoi("-91283472332")==-2147483648)
print(Solution().myAtoi("   -42")==-42)
print(Solution().myAtoi("4193 with words")==4193)
print(Solution().myAtoi("words and 987")==0)
print(Solution().myAtoi("")==0)
print(Solution().myAtoi("    -")==0)
print(Solution().myAtoi("+1")==1)
print(Solution().myAtoi("+-2")==0)
print(Solution().myAtoi("-+2")==0)