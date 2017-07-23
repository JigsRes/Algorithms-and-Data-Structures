# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.
#
# For example, given nums = [-2, 0, 1, 3], and target = 2.
#
# Return 2. Because there are two triplets which sums are less than 2: [-2, 0, 1][-2, 0, 3]

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