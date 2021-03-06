##TLE for Recursive, Therefore use memoization DP

# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.




class Solution(object):
    def __init__(self):
        self.count=0

    def numDistinct(self, s, t):
        dp=[[0]*(len(s)+1) for _ in xrange(len(t)+1)]
        print "initialize dp"
        dp[0]=[1]*(len(s)+1)

        # for j in range(1,len(t)+1):
        #     dp[0][j]=0
        for i in xrange(1,len(t)+1):
            for j in xrange(1,len(s)+1):
                if s[j-1]==t[i-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j]=dp[i][j-1]
        return dp[len(t)][len(s)]




    def numDistinctRecursive(self, s, t):
        len_t=len(t)
        len_s=len(s)
        if len_s<len_t:
            return 0

        def compare(pnt_s, pnt_t):
            if pnt_t >= len_t:
                self.count += 1
                return
            if pnt_s>=len_s:
                return
            if s[pnt_s]==t[pnt_t]:
                compare(pnt_s+1, pnt_t+1)
                compare(pnt_s+1, pnt_t)
            else:
                compare(pnt_s + 1, pnt_t)
        compare(0,0)
        return self.count



obj =Solution()
print obj.numDistinct("rabbbit","rabbit")