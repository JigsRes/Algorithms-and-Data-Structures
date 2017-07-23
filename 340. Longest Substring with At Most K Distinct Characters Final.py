# Given a string, find the length of the longest substring T that contains at most 2 distinct characters.
#
# For example, Given s = “eceba”,
#
# T is "ece" which its length is 3.


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            print i, c
            d[c]=i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
                print "Here"
            print low, "low"
            print i-low+1, "curr len"
            ret = max(i - low + 1, ret)
        return ret


if __name__=="__main__":
    obj= Solution()
    print(obj.lengthOfLongestSubstringKDistinct("abcdefgfgfgfgfgfhklm",2))
