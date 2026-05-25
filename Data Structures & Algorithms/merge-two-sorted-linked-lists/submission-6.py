# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        c1, c2 = list1 if list1.val >= list2.val else list2, list2 if list2.val <= list1.val else list1
        head = c2
        while c2.next and c2.next.val <= c1.val:
            c2 = c2.next
        curr = c2
        while c1 and c2:
            if c2.val <= c1.val and curr == c2:
                temp = c2.next
                c2.next = c1
                c2 = temp
                if not c2:
                    break
                while c1.next and c1.next.val <= c2.val:
                    c1 = c1.next
                curr = c1
            else:
                temp = c1.next
                c1.next = c2
                c1 = temp
                if not c1:
                    break
                while c2.next and c2.next.val <= c1.val:
                    c2 = c2.next
                curr = c2
        return head
                
            





