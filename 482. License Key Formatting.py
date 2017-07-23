# Now you are given a string S, which represents a software license key which we would like to format. The string S is composed of alphanumerical characters and dashes. The dashes split the alphanumerical characters within the string into groups. (i.e. if there are M dashes, the string is split into M+1 groups). The dashes in the given string are possibly misplaced.
#
# We want each group of characters to be of length K (except for possibly the first group, which could be shorter, but still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally, all the lower case letters in the string must be converted to upper case.
#
# So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need to return the license key formatted according to the description above.
#
# Example 1:
# Input: S = "2-4A0r7-4k", K = 4
#
# Output: "24A0-R74K"
#
# Explanation: The string S has been split into two parts, each part has 4 characters.
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        S=S.upper()
        string= list(S)
        new_list=[]
        i=1
        while(string):
            if(i%(K+1)==0):
                new_list.append('-')
                i+=1
            if(string[-1]=='-'):
                string.pop()
                continue
            else:
                new_list.append(string.pop())
                i+=1
        if(len(new_list)==0):
            return ""
        new_list=new_list[::-1]
        if new_list[0]=='-':
            new_list=new_list[1:]
        return ''.join(new_list)




obj=Solution()
print obj.licenseKeyFormatting("2-4A0r7-4k",4)