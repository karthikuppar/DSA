class Solution:
    def longestConsecutive(self, nums):
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num-1 not in num_set:
                current=num
                large=1
                while current+1 in num_set:
                    current+=1
                    large+=1
                longest=max(longest,large)
        return longest
a=Solution()
nums=[100, 4, 200, 1, 3, 2]
print(a.longestConsecutive(nums))

            
        




