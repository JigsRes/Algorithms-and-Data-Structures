class Solution(object):
    def getMinimumDifference(self, root):

        def __init__(self):
            self.prev_val = None
            self.mininum_difference = 0x7FFFFFFF

        def inorderTraverse(node):
            if not node:
                return self.mininum_difference

            inorderTraverse(node.left)
            if self.prev_val:
                self.mininum_difference = min(self.mininum_difference, node.val - self.prev_val)

            self.prev_val = node.val

            inorderTraverse(node.right)

        inorderTraverse(root)
        return self.mininum_difference

