# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
# (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
# Example:
#
# Given [3, 1, 5, 8]
#
# Return 167

#Idea is like
#For each k from 2 to n. (Group size)
#   For left-right of range [of group size selected by k] beginning from 0
#       Burst (left+1 to right-1) balloon one by one in the end and select max




def maxCoins( iNums):
    nums = [1] + [i for i in iNums if i > 0] + [1]
    print "nums", nums
    n = len(nums)
    dp = [[0]*n for _ in xrange(n)]
    print "initialize dp" ,dp
    for k in xrange(2, n):
        print "for k", k, dp
        print "look at k-1", k-1 , "baloons."
        for left in xrange(0, n - k):
            print  "for left", left, "and right", left+k
            right = left + k
            for i in xrange(left + 1,right):
                print "i", i,"dp of",left,right , "is max of",  dp[left][right],  nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                dp[left][right] = max(dp[left][right],
                       nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][n - 1]



print maxCoins([3, 1, 5, 8,6])