# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        n = head.next
        head.next = None
        while n:
            nn = n.next
            n.next = head
            head = n
            n = nn
        return head