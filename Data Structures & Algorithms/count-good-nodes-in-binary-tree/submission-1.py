# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root: Optional[TreeNode], max: int):
            nonlocal res
            if not root:
                return
            if max <= root.val:
                res += 1
                max = root.val
            dfs(root.left, max)
            dfs(root.right, max)
            
        dfs(root, root.val)
        return res