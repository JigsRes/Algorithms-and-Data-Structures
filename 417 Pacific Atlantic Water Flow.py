# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# Example:
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

class Solution(object):
    def pacificAtlantic(self, matrix):
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [False for _ in xrange(rows * cols)]
        pacific = set()
        atlantic = set()

        def isreachable(height, a, b):
            return True if 0 <= a < rows and 0 <= b < cols and height <= matrix[a][b] else False

        def visit(m, n, ocean):
            if m * cols + n not in ocean:
                ocean.add(m * cols + n)
                value = matrix[m][n]
                reachable = filter(lambda (val, x, y): isreachable(val, x, y),
                                   [(value, m + 1, n), (value, m - 1, n), (value, m, n + 1), (value, m, n - 1)])
                for val, x, y in reachable:
                    visit(x, y, ocean)

        for i in xrange(rows):
            if i * cols not in pacific:
                visit(i, 0, pacific)

        for j in xrange(cols):
            if j not in pacific:
                visit(0, j, pacific)

        for i in xrange(rows):
            if i * cols + (cols - 1) not in atlantic:
                visit(i, cols - 1, atlantic)

        for j in xrange(cols):
            if (rows - 1) * cols + j not in atlantic:
                visit(rows - 1, j, atlantic)
        result = []
        for val in pacific & atlantic:
            result.append([val // cols, val % cols])
        return result


obj=Solution()
print obj.pacificAtlantic([[1]])