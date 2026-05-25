# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        last = head
        n = 1
        while last and last.next:
            n += 1
            last = last.next
        idx = n // 2
        k = head
        half = k
        t = 1
        while k and k.next:
            k = k.next
            if t == idx:
                half = k
                break
            t+=1
        print(n, half.val)
        n-=1
        curr = head.next
        head.next = last
        while curr:
            last.next = curr
            if curr == half:
                half.next = None
                break
            k = curr
            temp = curr.next
            for _ in range(n-2):
                k = k.next
            n -= 2
            last = k
            curr.next = last
            curr = temp
            
