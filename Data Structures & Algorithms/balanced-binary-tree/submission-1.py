# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def check(curr):
            if not curr:
                return 0

            left = check(curr.left)
            right = check(curr.right)

            if left - right > 1 or right - left > 1:
                return -1

            if left == -1 or right ==-1:
                return -1

            return 1 + max(left, right)
        a = check(root)
        if a >= 0:
            return True
        return False

            
        