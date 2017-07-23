



def solution():
    X = int(raw_input())
    N = int(raw_input())

    dp=[1]+[0]*X
    for i in range(1, X+1):
        num=pow(i,N)
        if num>X:
            break
        print i, num
        for j in range( X, num-1, -1):
            print j,num
            dp[j]+=dp[(j-num)]
    return dp[-1]


print solution()
