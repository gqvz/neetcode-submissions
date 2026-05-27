# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root: Optional[TreeNode], min: int, max:int):
            nonlocal res
            if not root:
                return
            res &= min < root.val < max
            dfs(root.right, root.val, max)
            dfs(root.left, min, root.val)
        if not root:
            return True
        dfs(root.right, root.val, 1001)
        dfs(root.left, -1001, root.val)
        return res