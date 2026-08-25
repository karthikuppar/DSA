class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum is on the right side
                left = mid + 1
            else:
                # Minimum is at mid or on the left side
                right = mid

        return nums[left]


a = Solution()

nums = [3, 4, 5, 6, 1, 2]

print(a.findMin(nums))