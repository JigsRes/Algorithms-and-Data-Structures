class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for k in range(len(nums)-2):
            i, j = k+1, len(nums)-1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j - i
                    i += 1
                else:
                    j -= 1
        return count

obj= Solution()
print obj.threeSumSmaller([0,-4,-1,1,-1,2], -5)


print "a".isdigit()