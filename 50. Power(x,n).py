class Solution(object):
    def myPow(self, x, n):

        def power(m):

            if m == 1:
                return x
            if m == 2:
                return x * x
            if m % 2 == 1:
                return x * power(m - 1)
            else:
                half_power = power(m/2)
                return half_power * half_power

        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        return power(n)

obj=Solution()
print obj.myPow(8.84372,-5)