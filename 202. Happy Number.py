# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Credits:
# Special thanks to @mithmatt and @ts for adding this problem and creating all test cases.
class Solution(object):
    def squaredNum(self, m):
        sum_square = 0
        while m!=0:
            print "start m" ,m
            digit = m % 10
            sum_square += digit ** 2

            m/=10
            print "end m",m

        return sum_square


    def isHappy(self, n):
        slow = n
        fast = n
        while True:
            slow = self.squaredNum(slow)
            fast = self.squaredNum(fast)
            fast = self.squaredNum(fast)
            print slow, fast
            if slow == fast:
                break
        if slow == 1:
            return True
        return False


obj=Solution()
print obj.isHappy(3)