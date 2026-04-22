class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
   

        firstIndex = 0
        while firstIndex < len(numbers) - 1:
            
            left = firstIndex
            rigth = len(numbers) - 1
            while left <= rigth:
                secondIndex = (left + rigth) // 2
                if numbers[firstIndex] + numbers[secondIndex] == target:
                    return [firstIndex + 1, secondIndex + 1]
                elif numbers[firstIndex] + numbers[secondIndex] > target:
                    rigth = secondIndex - 1
                else: 
                    left = secondIndex + 1
            
            firstIndex += 1
            
           
        return [-1 , -1]