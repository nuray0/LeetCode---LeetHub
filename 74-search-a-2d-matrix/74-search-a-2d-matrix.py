class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        while (len(matrix) > 0):
            rows = len(matrix)
            columns = len(matrix[0])

            i = rows // 2

            if target >= matrix[i][0] and target <= matrix[i][columns - 1]:
                if target in matrix[i]:
                    return True
                else:
                    return False
                
            elif target < matrix[i][0]:
                matrix = matrix[:i]
                
            elif target > matrix[i][columns - 1]:
                matrix = matrix[i + 1:]

        return False
