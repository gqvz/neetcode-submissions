# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = prev = copy = ListNode()
        carry = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode()
            if not l2:
                l2 = ListNode()
            sum = l1.val + l2.val + carry
            head.val = sum % 10
            carry = sum // 10
            head.next = ListNode()
            prev = head
            head = head.next
            l1 = l1.next
            l2 = l2.next
        if carry == 0:
            prev.next = None
        head.val = carry
        return copy
        