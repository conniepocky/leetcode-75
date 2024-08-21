class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        chars = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        results = []

        def backtrack(i, currentStr):
            if len(currentStr) == len(digits):
                results.append(currentStr)
                return

            for c in chars[digits[i]]:
                backtrack(i+1, currentStr + c)

        backtrack(0, "")

        return results
