# Leetcode15_threeSum.py


# Solution 1: similar to 2sum. Use -nums[i] as target instead and find elements that
# add up to target
# use left and right pointers to locate the elements being added up and compare

# O(n**2)

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            # print('i: ', i)
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1; right = len(nums) - 1
                # print('left: ', left, 'right', right)
                while left < right:
                    if nums[left] + nums[right] == -nums[i]:
                        # print('found it sum of -sum[i]:', -nums[i])
                        # print('num[left]', nums[left], ';', 'num[right]', nums[right])
                        ans.append([nums[i], nums[left], nums[right]])
                        left += 1; right -= 1
                        while left < right and nums[left] == nums[left-1]: # leave out duplicate numbers
                            left +=1
                        while left < right and nums[right] == nums[right+1]: # leave out duplicate numbers
                            right -= 1
                    elif nums[left] + nums[right] < -nums[i]: # if sum is smaller than target, increment left pointer
                        while left < right:
                            left += 1
                            break
                    else:
                        while left < right: # if sum is larger than target, decrement right pointer
                            right -= 1
                            break
        return ans


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1,-1,2],[-1,0,1]])



