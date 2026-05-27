# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = left = prev = ListNode()
        dummy.next = right = head
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next
        print(n // k)
        for _ in range(n // k):
            for _ in range(k):
                temp = right.next
                right.next = prev
                prev = right
                right = temp
                
            left.next.next = right
            temp = left.next
            left.next = prev
            left = prev = temp
        return dummy.next
        
