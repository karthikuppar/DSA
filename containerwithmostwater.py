class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1

        max_water = 0

        while left < right:

            width = right - left
            water_height = min(height[left], height[right])

            water = width * water_height

            max_water = max(max_water, water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


a = Solution()

height = [1, 7, 2, 5, 4, 7, 3, 6]

print(a.maxArea(height))