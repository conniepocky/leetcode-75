class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs = 0

        nums = sorted(nums)

        left = 0
        right = len(nums)-1

        while left < right:
            twosum = nums[left] + nums[right]
            if twosum == k:
                left += 1
                right -= 1

                pairs += 1
            elif twosum < k:
                left += 1
            else:
                right -= 1

        return pairs


