class Solution(object):
    def __init__(self):
        self.count=0
    def numDistinct(self, s, t):
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


obj=Solution()
print obj.numDistinct("rabbbit","rabbit")