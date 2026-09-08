class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) -1
        while low <= high:
            index = (low+high) // 2
            matrix_row = matrix[index]
            lower = 0
            higher = len(matrix_row) -1
            while lower <= higher:
                indexed = (lower+higher) // 2
                num = matrix_row[indexed]
                if num == target:
                    return True
                elif num < target:
                    lower = indexed + 1
                elif num > target:
                    higher = indexed -1
            if matrix_row[0] > target:
                high = index -1
            else:
                low = index + 1
        return False

                
        