class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowct, colct = len(matrix), len(matrix[0])
        t, b = 0, rowct - 1

        while t <= b:
            row = (t + b) // 2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break

        if not (t <= b):
            return False

        row = (t + b) // 2
        l, r = 0, colct - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1 
            else:
                return True
        return False