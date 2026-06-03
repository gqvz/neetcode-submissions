"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        q.append(node)
        n = Node(node.val)
        m = {}
        m[node] = n
        while q:
            o = q.popleft()
            for neighbor in o.neighbors:
                if neighbor not in m:
                    m[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                m[o].neighbors.append(m[neighbor])
        return n