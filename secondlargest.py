class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)
        
        if n < 2:
            return -1

        large = float('-inf')
        second_large = float('-inf')

        for i in range(n):
            if nums[i] > large:
                second_large = large
                large = nums[i]
            elif nums[i] > second_large and nums[i] != large:
                second_large = nums[i]

        return second_large if second_large != float('-inf') else -1


a = Solution()
nums = [10,10,10,10,10]
print(a.secondLargestElement(nums))