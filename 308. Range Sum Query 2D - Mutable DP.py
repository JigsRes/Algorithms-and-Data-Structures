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
        self.mylist=matrix
        self.row_len= len(matrix[0]) #length of row = number of columns
        self.col_len=len(matrix) #length of col = number of rows
        self.my_matrix=[[0 for i in range(self.row_len+1)] for j in range(self.col_len+1)]

        for i in range(self.col_len):
            for j in range(self.row_len):
                self.my_matrix[i+1][j+1]=self.my_matrix[i][j+1]+self.my_matrix[i+1][j]+matrix[i][j]-self.my_matrix[i][j]
        #print self.my_matrix


    def update(self, row, col, val):

        difference= val - self.mylist[row][col]
        self.mylist[row][col]=val
        for i in range(row+1, self.col_len+1):
            for j in range(col+1, self.row_len+1):
                self.my_matrix[i][j]+=difference


    def sumRegion(self, row1, col1, row2, col2):

        return self.my_matrix[row2+1][col2+1]- self.my_matrix[row2+1][col1]-self.my_matrix[row1][col2+1]+self.my_matrix[row1][col1]

if __name__=="__main__":
    #["NumMatrix", "update", "update", "update", "sumRegion"]
    #[[[[2,4],[-3,5]]],[0,1,3],[1,1,-3],[0,1,1],[0,0,1,1]]
    matrix=[[2,4],[-3,5]]
    obj = NumMatrix(matrix)
    obj.update(0,1,3)
    obj.update(1,1,-3)
    obj.update(0,1,1)
    print obj.sumRegion(0,0,1,1)



