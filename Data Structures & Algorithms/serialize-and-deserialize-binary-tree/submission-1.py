# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        thing = []
        while q:
            k = q.popleft()
            if k:
                q.append(k.left)
                q.append(k.right)
            thing.append(str(k.val) if k else 'null')
        return ','.join(thing)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = deque()
        arr = [int(d) if d.isdigit() else None for d in data.split(',')]
        r = arr.pop(0)
        root = TreeNode(val=r) if r else None
        q.append(root)
        while q:
            k = q.popleft()
            if k:
                l = arr.pop(0)
                r = arr.pop(0)
                if l:
                    k.left = TreeNode(val=l)
                    q.append(k.left)
                if r:
                    k.right = TreeNode(val=r)
                    q.append(k.right)

        return root












