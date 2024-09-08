class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        left = 0
        count = 0
        maxCount = 0

        for right in range(len(s)):
            if right-left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                left += 1

            if s[right] in vowels:
                count += 1
                maxCount = max(count, maxCount)

        return maxCount
