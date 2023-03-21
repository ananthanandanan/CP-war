from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        if len(matrix) == 1:
            return target in matrix[0]

        for row in matrix:
            if row[0] <= target <= row[-1]:
                l, r = 0, len(row) - 1
                while l <= r:
                    mid = l + (r-l)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
        return False