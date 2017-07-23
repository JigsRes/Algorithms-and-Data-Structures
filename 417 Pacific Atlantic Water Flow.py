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