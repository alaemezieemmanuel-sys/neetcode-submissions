# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(root):
            current = root
            if not current.left and not current.right:
                return
            if current.left and current.right:
                current.left, current.right = current.right, current.left
                recur(current.left)
                recur(current.right)
            elif current.right:
                current.left = current.right
                current.right = None
                recur(current.left)
            else:
                current.right= current.left
                current.left = None
                recur(current.right)
        if root is None:
            return
        recur(root)
        return root
        
        