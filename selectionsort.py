class Solution:
    def selectionSort(self, nums):
        n=len(nums)
        for i in range(n):
            minimum_index=i
            for j in range(i+1,n):
                if nums[j]<nums[minimum_index]:
                    minimum_index=j
            nums[i],nums[minimum_index]=nums[minimum_index],nums[i]
        return nums
a=Solution()
nums=[5,4,4,1,1]
print(a.selectionSort(nums))


        