class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        counts1 = {}
        counts2 = {}

        for i in word1:
            if i not in counts1:
                counts1[i] = 0
            counts1[i] += 1

        for i in word2:
            if i not in counts2:
                counts2[i] = 0
            counts2[i] += 1

        vals1 = sorted(list(counts1.values()))
        vals2 = sorted(list(counts2.values()))

        if vals1 != vals2:
            return False

        return True
