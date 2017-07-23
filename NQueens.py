class Solution(object):
    def solveNQueens(self, n):
        solution = [[0 for _ in xrange(n)] for _ in xrange(n)]
        result = []

        def isSafe(solution, row, col):
            for j in range(col):
                if solution[row][j] == 1:
                    return False
                if 0 <= j - col + row < n and solution[j - col + row][j] == 1:
                    return False
                if 0 <= row - j + col < n and solution[row - j + col][j] == 1:
                    return False
            return True

        def solveNQueensUtil(solution, col):
            print "Solve column", col
            if col == n:
                print "adding result", solution
                curr_result=[]
                for x in range(n):
                    for y in range(n):
                        if solution[x][y]==1:
                            curr_result.append("."*y+"Q"+"."*(n-y-1))
                            continue
                result.append(curr_result)
                print result
                return

            for row in range(n):
                for j in range(col, n):
                    for i in range(n):
                        solution[i][j] = 0

                print "Trying row", row, "for col", col

                if isSafe(solution, row, col):
                    solution[row][col] = 1
                    print "current solution", solution
                    print "It is safe so solve next column"
                    solveNQueensUtil(solution, col + 1)


        solveNQueensUtil(solution, 0)

        return result

obj =Solution()
print obj.solveNQueens(4)