class Solution:
    def countFrequencies(self, nums):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        result = []
        for key in freq:
            result.append([key, freq[key]])

        return result
a = Solution()
nums = [1, 2, 2, 3, 3, 3, 4]
print(a.countFrequencies(nums))