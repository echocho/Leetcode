class Solution:
    # O(m + n)
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not m:
            nums1[:] = nums2[:]
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1   
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1. # only return for testing
print(Solution().merge([1,2,3,0,0,0],3,[2,5,6],3) == [1,2,2,3,5,6])
print(Solution().merge([1,2,3,4,0,0,0],4,[2,5,6],3)== [1,2,2,3,4,5,6])  #  == [1,2,2,3,4,5,6]
print(Solution().merge([1,2,0,0,0],2,[2,5,6],3)== [1,2,2,5,6]) #  
print(Solution().merge([0,0,0],0,[2,5,6],3)== [2,5,6]) # 
print(Solution().merge([2,0],1,[1],1)==[1,2]) # 
