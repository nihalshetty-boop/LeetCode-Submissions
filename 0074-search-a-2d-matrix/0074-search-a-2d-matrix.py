class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowct, colct = len(matrix), len(matrix[0])
        l, r = 0, (rowct * colct) - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // colct, m % colct
            if matrix[row][col] < target:
                l = m + 1
            elif matrix[row][col] > target:
                r = m - 1 
            else:
                return True
        return False