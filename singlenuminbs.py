class Solution:
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Pair is correct, single is on the right
                left = mid + 2
            else:
                # Pair is broken, single is on the left
                right = mid

        return nums[left]


a = Solution()

nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]

print(a.singleNonDuplicate(nums))