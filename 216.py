class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(i, path, currentSum):
            if len(path) == k and currentSum == n:
                results.append(path)
                return
            elif len(path) == k and currentSum != n:
                return

            for num in range(i, 10):
                backtrack(num+1, path+[num], currentSum + num)

        backtrack(1, [], 0)

        return results
