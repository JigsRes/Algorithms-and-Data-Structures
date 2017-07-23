class Solution(object):


    def solveSudoku(self, board):
        mat_board = []
        rows=[set() for _ in xrange(9)]
        cols=[set() for _ in xrange(9)]
        bloacks=[set() for _ in xrange(9)]
        for row in board:
            mat_board.append(list(row))

        def isValid(m,n,value):

        def solve(i,j):
            if i>9 and j>9:
                return True

            for val in range(1,10):
                mat_board[i][j] = val
                if isValid(i,j,val):
                    if j<9:
                        return solve(i,j+1)
                    else:
                        return solve(i+1,0)
            mat_board[i][j]="."
            return False




        solve(0,0)













obj=Solution()
obj.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])