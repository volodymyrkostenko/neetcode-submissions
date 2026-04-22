class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        rigth = len(nums) - 1

        count = 0  
           
        while left <= rigth:    
            i = round((left + rigth) / 2)
            if target == nums[i]:
                return i
            elif target > nums[i]:
                left = i + 1
            else: 
                rigth = i - 1

            count += 1


        return -1