class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)

        pairs = []

        for i in spells:
            low = 0
            high = len(potions)-1
            ind = len(potions)

            while low <= high:
                mid = (low+high) //2
                if i * potions[mid] >= success:
                    high = mid-1
                    ind = mid
                else:
                    low = mid+1

            pairs.append(len(potions)-ind)

        return pairs
