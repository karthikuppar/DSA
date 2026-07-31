class Solution:
    def trap(self, height):
        water=0
        n=len(height)
        for i in range(n):
            left=0
            right=0
            for j in range(i+1):
                left=max(left,height[j])
            for j in range(i,n):
                right=max(right,height[j])
            water+=min(left,right)-height[i]
        return water
a=Solution()
height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(a.trap(height))

#optimal solution 
'''
class Solution:
    def trap(self, height):
        water=0
        n=len(height)
        left=0
        right=n-1
        maxleft=0
        maxright=0
        while left<=right:
            if height[left]<=height[right]:
                if height[left]>=maxleft:
                    maxleft=height[left]
                else:
                    water+=maxleft-height[left]
                left+=1
            else:
                if height[right]>=maxright:
                    maxright=height[right]
                else:
                    water+=maxright-height[right]
                right-=1
        return water
a=Solution()
height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(a.trap(height))        
        '''
       