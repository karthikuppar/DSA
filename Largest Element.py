class Solution:
    def largestElement(self, nums):
        n=len(nums)
        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j]>nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[n-1]
a=Solution()
nums=[3,3,0,99,-40]
print(a.largestElement(nums))
        