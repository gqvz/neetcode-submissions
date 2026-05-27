# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque()
        result = []
        dummy = TreeNode()
        q.append(root)
        q.append(dummy)
        c = []
        while q:
            k = q.popleft()
            if k == dummy:
                result.append(c)
                c = []
                if not q:
                    break
                q.append(dummy)
                continue
            c.append(k.val)
            if k.left:
                q.append(k.left)
            if k.right:
                q.append(k.right)
        return result