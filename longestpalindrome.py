class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        length = 0

        for char in s:
            if char not in odd:
                odd.add(char)
            else: #double number, even
                odd.remove(char) 
                length += 2

        if odd: #middle number
            length +=1

        return length
