class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        res = 0
        count = 0

        while i < len(chars):
            print(res)
            current = chars[i]
            count = 0

            while i < len(chars) and chars[i] == current:
                count += 1
                i += 1

            chars[res] = current
            res += 1

            if count > 1:
                for c in str(count):
                    chars[res] = c
                    res += 1

        return res
