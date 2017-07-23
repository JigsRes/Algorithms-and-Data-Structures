# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
#
# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]


class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []
        num_row = len(matrix)
        num_col = len(matrix[0])
        #rev_matrix = zip(*matrix)

        result = []
        for i in range(num_row + num_col):
            if i%2==0:
                row = i
                col = 0
                if i>=num_row:
                    differnce = i - num_row + 1
                    row-=differnce
                    col+=differnce
                while col < num_col and row >= 0:
                    # print row, col, "time" , i
                    result.append(matrix[row][col])
                    col += 1
                    row -= 1
            else:
                col = i
                row = 0
                if i>=num_col:
                    differnce=i-num_col+1
                    col-=differnce
                    row+=differnce
                while row < num_row and col >= 0:
                    # print row, col, "time", i
                    result.append(matrix[row][col])
                    row += 1
                    col -= 1
        return result



obj = Solution()
print obj.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])



print obj.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ]
])


print obj.findDiagonalOrder([
 [ 1, 2, 3 ]
])

