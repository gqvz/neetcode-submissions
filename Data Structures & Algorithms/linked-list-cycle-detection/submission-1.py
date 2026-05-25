# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False
        a = head
        b = head.next.next
        while a and b and a.next and b.next and b.next.next:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False
