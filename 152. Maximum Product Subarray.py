
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        dp_positive = max(0, nums[0])
        dp_negative = min(0, nums[0])
        global_max = nums[0]
        for num in nums[1:]:
            if num > 0:
                dp_positive = max(num, num * dp_positive)
                dp_negative = num * dp_negative
            else:
                dp_positive = num * dp_negative
                dp_negative = min(num, num * dp_positive)
            global_max = max(dp_positive, global_max)
        return global_max