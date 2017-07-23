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