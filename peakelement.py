import numpy as np

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        if len(nums) == 2:
            return np.argmax(nums)

        while low < high:
            mid = int((low+high) / 2)

            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid+1] > nums[mid-1]:
                low = mid+1
            else:
                high = mid-1

        return low
