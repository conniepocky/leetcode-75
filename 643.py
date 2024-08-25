class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = maxSum = sum(nums[:k])

        for i in range(k, len(nums)):
            current += nums[i] - nums[i-k]

            maxSum = max(current, maxSum)

        return maxSum / k
