class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = set()
        nums = {}

        for x in arr:
            if x not in nums:
                nums[x] = 0
            nums[x] += 1

        for x in nums.values():
            if x in occurences:
                return False
            occurences.add(x)

        return True
