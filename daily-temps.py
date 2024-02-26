class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        idx = []

        for i,v in enumerate(temperatures):
            while idx and v > idx[-1][1]:
                stackInd = idx.pop()[0]
                result[stackInd] = i-stackInd 

            idx.append([i,v])

        return result

