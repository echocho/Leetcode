# leetcode_136_singleNumber.py
def singleNumber(nums):
    a = set()
    for num in nums:
        if num not in a:
            a.add(num)            
        else:
           a.remove(num)
    for res in a:
        return res  
print(singleNumber([1,2,3,4,5,6,5,4,3,2,1]))