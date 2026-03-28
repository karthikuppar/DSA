class Solution:
    def mostFrequentElement(self, nums):
        fre={}
        for i in nums:
            if i in fre:
                 fre[i]+=1
            else:
                 fre[i]=1
        for key in fre:
            if fre[key]==max(fre.values()):
                return key
a=Solution()
nums=[1,2,2,3,3,3,4]
print(a.mostFrequentElement(nums))
        
     