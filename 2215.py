class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)

        distinct1, distinct2 = [], []

        for i in s1:
            if i not in s2:
                distinct1.append(i)

        for i in s2:
            if i not in s1:
                distinct2.append(i)

        return [distinct1, distinct2]
