#Source: https://leetcode.com/
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
#
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

class NumMatrix(object):
    def __init__(self, matrix):
        self.mylist = matrix

    def update(self, row, col, val):
        self.mylist[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        sum = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                sum += self.mylist[i][j]
        return sum


if __name__=="__main__":
    matrix=[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    obj = NumMatrix(matrix)
    print obj.sumRegion(2,1,4,3)
    obj.update(3,2,2)
    print obj.sumRegion(2, 1, 4, 3)



