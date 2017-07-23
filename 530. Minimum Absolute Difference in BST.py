# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
#
# Example:
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


class Solution(object):
    def __init__(self):
        self.prev_val = None
        self.mininum_difference = 0x7FFFFFFF

    def getMinimumDifference(self, root):

        def inorderTraverse(node):

            if not node:
                return
            print "visiting", node.val
            print "prev_val", self.prev_val

            inorderTraverse(node.left)

            if self.prev_val != None:
                self.mininum_difference = min(self.mininum_difference, node.val - self.prev_val)
            self.prev_val = node.val

            inorderTraverse(node.right)

        inorderTraverse(root)
        return self.mininum_difference