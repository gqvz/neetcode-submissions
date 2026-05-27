class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        
        def build(pre_l, pre_r, in_l, in_r):
            if pre_l > pre_r:
                return None
            root_val = preorder[pre_l]
            node = TreeNode(val=root_val)
            mid = idx_map[root_val]
            left_size = mid - in_l
            node.left = build(pre_l+1, pre_l+left_size, in_l, mid-1)
            node.right = build(pre_l+left_size+1, pre_r, mid+1, in_r)
            return node
        
        return build(0, len(preorder)-1, 0, len(inorder)-1)