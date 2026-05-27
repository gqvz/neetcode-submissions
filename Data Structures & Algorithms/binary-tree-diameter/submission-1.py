# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + max(depth(root.right), depth(root.left))
        if not root:
            return 0
        return max(depth(root.left) + depth(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))