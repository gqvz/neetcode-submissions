"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        nh = Node(head.val)
        curr = nh
        last = None
        node_to_n = {}
        n_to_node = {}
        n = 0
        while head and head.next:
            node_to_n[head] = n
            n_to_node[n] = curr
            nn = Node(head.next.val)
            curr.next = nn
            curr = nn
            head = head.next
            n+=1
        node_to_n[head] = n
        n_to_node[n] = curr
        for (key, val) in node_to_n.items():
            random = key.random
            if not random:
                n_to_node[val].random = last
                continue
            n_to_node[val].random = n_to_node[
                node_to_n[random]]
        curr.next = last
        return nh

        