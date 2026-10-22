# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = 0
        current = root
        stack = []
        

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            num+=1

            if num == k:
                return current.val
            current = current.right
        