class Solution:
    def findPeakElement(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                # We are going uphill
                # A peak must exist on the right
                left = mid + 1
            else:
                # We are going downhill
                # A peak is at mid or on the left
                right = mid

        return left