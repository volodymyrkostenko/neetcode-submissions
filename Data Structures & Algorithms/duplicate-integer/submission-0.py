class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        while(len(nums) > 0):
            el = nums.pop(0)
            if(el in nums):
                return True
        return False
            
        