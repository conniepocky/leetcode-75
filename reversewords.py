class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        string = ""

        wordsReversed = []

        for ind in range(len(s)):
            if s[ind] == " ":
                words.append(string)
                string = ""
            elif ind == len(s)-1:
                string = string + s[ind]
                words.append(string)
            else:
                string = string + s[ind]

        for i in range(len(words),0,-1):
            if words[i-1] != "":
                wordsReversed.append(words[i-1])

        return " ".join(wordsReversed)


