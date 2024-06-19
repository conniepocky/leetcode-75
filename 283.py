class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        c = 0 
        for f in range(len(nums)):
            if nums[f] != 0:
                nums[f], nums[c] = nums[c], nums[f] #swap when find val not equal to zero

                c += 1
                
        
