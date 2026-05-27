# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q: return True
            if (p and not q) or (not p and q): return False
            return p.val == q.val and same(p.left, q.left) and same(p.right, q.right) 

        res = same(root, subRoot)
        def dfs(root: Optional[TreeNode]):
            nonlocal res
            if not root:
                return 0
            if same(root.left, subRoot) or same(root.right, subRoot):
                res = True
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res