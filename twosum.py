class Solution:
    def twoSum(self, nums, target):
        hashmap={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[nums[i]]=i
a=Solution()
nums = [1, 3, 5, -7, 6, -3]
target =0
print(a.twoSum(nums, target))