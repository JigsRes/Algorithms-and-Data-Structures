class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        j = 0
        while j < len(t) and i < len(t):
            print i, j
            if s[i] == t[j]:
                print "match", s[i], t[j]
                i += 1
                j += 1
            else:
                j += 1

        return i == len(t)


obj=Solution()
print obj.isSubsequence("abc","ahbgdc")