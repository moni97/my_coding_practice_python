class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])
        row = 0
        while l <= r and row < len(matrix):
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif target > matrix[row][len(matrix[0]) - 1]:
                row += 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
