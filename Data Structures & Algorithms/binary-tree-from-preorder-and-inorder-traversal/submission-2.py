# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(inorder) == 1:
            return TreeNode(val=inorder[0])
        root = preorder[0]
        # print(preorder, inorder)
        idx = inorder.index(root)
        node = TreeNode(val=root)
        end = -(len(inorder)-idx)+1 or None
        lp, li = preorder[1:end], inorder[:idx]
        rp, ri = preorder[idx+1:], inorder[idx+1:]
        # print("LEFT ", lp, li)
        # print("RIGHT ", rp, ri)
        node.left = self.buildTree(lp, li)
        node.right = self.buildTree(rp, ri)

        return node