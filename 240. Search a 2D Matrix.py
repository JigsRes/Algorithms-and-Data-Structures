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