# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that
# the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container
# contains the most water.
#
# Note: You may not slant the container and n is at least 2.


class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = float('-inf')

        while l < r:
            if height[l] <= height[r]:
                # find next max l
                curr = height[l]
                curr_l = l
                l += 1
                while (l < len(height) and curr >= height[l]):
                    l += 1
                max_area = max(max_area, curr * (l - curr_l))
            elif height[l] > height[r]:
                curr = height[r]
                curr_r = r
                r -= 1
                while (r > 0 and curr >= height[r]):
                    r -= 1
                max_area = max(max_area, curr * (curr_r - r))
        return max_area


obj=Solution()
print obj.maxArea([3,1,1,3,4])