# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
#
# For example, Given s = “eceba”,
#
# T is "ece" which its length is 3.


#Time Limit Exceeded
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return 0
        maxlength = 0
        for i in range(len(s)):
            currlist = []
            distinct = 0

            for j in range(i, len(s)):
                if s[j] not in currlist:
                    distinct += 1
                    currlist.append(s[j])
                    if distinct > k:
                        maxj = j - 1
                        break

                maxj = j
            curr_maxlen = maxj - i + 1
            if curr_maxlen > maxlength:
                maxlength = curr_maxlen
        return maxlength


if __name__=="__main__":
    obj= Solution()
    print(obj.lengthOfLongestSubstringKDistinct("aa",1))
