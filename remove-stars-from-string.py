class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        for i,v in enumerate(s):
            if v != "*":
                output.append(v)
            else:
                output.pop()

            i += 1
            
        return "".join(output)
