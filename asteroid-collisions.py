import numpy as np

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []

        for a in asteroids:
            while result != [] and a < 0 and result[-1] > 0: #if a -ive and previous is positive
                if abs(a) > result[-1]: #if asteroid is bigger than previous
                    result.pop()
                elif result[-1] > abs(a): #if previous is larger than asteroid
                    break
                elif a + result[-1] == 0: #if both are equal in size
                    result.pop()
                    break
            else:
                result.append(a)

        return result
