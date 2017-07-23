class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        if not nums:
            return []

        j=lower
        pnt=0
        result=[]
        while lower<=j<=upper and pnt < len(nums):

            if nums[pnt]==j:
                j+=1
                pnt+=1

            elif nums[pnt]>j:
                first_val=j
                second_val=nums[pnt]-1
                if first_val==second_val:
                    result.append(str(first_val))
                else:
                    result.append(str(first_val)+"->"+str(second_val))
                j=nums[pnt]+1
                pnt+=1
            elif nums[pnt] < j:
                pnt += 1

        if upper>j:
            result.append(str(j) + "->" + str(upper))
        if upper==j:
            result.append(str(j))
        return result


obj=Solution()
print obj.findMissingRanges([-2147483648,-2147483648,0,2147483647,2147483647],
-2147483648,
2147483647)