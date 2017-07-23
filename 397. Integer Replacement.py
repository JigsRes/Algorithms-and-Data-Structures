import math

class Solution(object):
    def integerReplacement(self, n):
        if n==1:
            return 0
        count=0
        while n!=1:
            print n
            if ((n != 0) and ((n & (~n + 1)) == n)):
                    return count+int(math.log(n,2))
            if n%2==0:
                n=n/2
            else:
                dec_num=n-1
                if ((dec_num != 0) and ((dec_num & (~dec_num + 1)) == dec_num)):
                    return count+int(math.log(dec_num,2))+1
                inc_num=n+1
                if ((inc_num != 0) and ((inc_num & (~inc_num + 1)) == inc_num)):
                    return count+int(math.log(inc_num,2))+1
                n=n+1
            count+=1
        return count


obj=Solution()
print obj.integerReplacement(10000)