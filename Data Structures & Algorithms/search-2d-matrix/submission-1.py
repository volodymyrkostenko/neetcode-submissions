class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            for el in row:
                arr.append(el)


        left = 0
        rigth = len(arr) - 1

        print(arr)

        while left <= rigth:
            mid = (left + rigth) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else: 
                rigth = mid - 1
        return False

        