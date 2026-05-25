# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Base case: 0, 1, or 2 nodes require no reordering
        if not head or not head.next or not head.next.next:
            return
        
        curr = head
        # We only need to weave if there are at least 2 nodes ahead of us
        while curr and curr.next and curr.next.next:
            
            # 1. Traverse to find the second-to-last node
            prev = curr
            while prev.next.next:
                prev = prev.next
            
            # 2. Isolate the last node (tail)
            tail = prev.next
            prev.next = None
            
            # 3. Weave: Insert tail between curr and curr.next
            tail.next = curr.next
            curr.next = tail
            
            # 4. Move forward to the next original node
            curr = tail.next