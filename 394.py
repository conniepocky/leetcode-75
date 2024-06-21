class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            string = ""

            if s[i] != "]":
                stack.append(s[i])
            else:
                while stack[-1] != "[":
                    string = stack.pop() + string
                stack.pop()

                n = ""

                while stack and stack[-1].isdigit():
                    n = stack.pop() + n

                for count in range(0, int(n)):
                    stack.append(string)


        return "".join(stack)
                    

                                
