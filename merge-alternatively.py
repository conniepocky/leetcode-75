class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        totalLen = len(word1) + len(word2)

        for i,v in enumerate([*word1]):
            word.append(v)
            if len(word2) <= i:
                break
            word.append(word2[i])

        if len(word) != totalLen:
            lenDiff = totalLen - len(word) 
            if len(word1) < len(word2):
                wrd = word2[::-1]
                print(wrd)
                for i in wrd[lenDiff-1::-1]:
                    word.append(i)
            else:
                wrd = word1[::-1]
                for i in wrd[lenDiff-1::-1]:
                    word.append(i)

        return "".join(word)
        
