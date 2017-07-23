# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
#
# Consider the following matrix:
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
# Given target = 5, return true.
#
# Given target = 20, return false.

class Solution(object):
    def searchMatrix(self, matrix, target):
        i = 0
        rows = len(matrix)
        j = 0
        cols = len(matrix[0])
        def visit(i,j):
            if i>=rows or j>=cols:
                return False
            if matrix[i][j]==target:
                return True
            return any(map(visit,(i,i+1),(j+1,j)))


        return visit(0,0)

obj=Solution()
print obj.searchMatrix(
  [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
,19)


# while i < rows and j < cols:
#     print "Discovered" , matrix[i][j]
#     if matrix[i][j] == target:
#         return True
#     if j + 1 < cols and matrix[i][j + 1] <= target:
#         j += 1
#         print "moving right"
#     elif i + 1 < rows and matrix[i + 1][j] <= target:
#         i += 1
#         print "moving down"
#     else:
#         return False