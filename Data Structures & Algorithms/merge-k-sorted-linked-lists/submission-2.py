# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = head = ListNode()
        while any(lists):
            idx = min([(i, curr.val) for i, curr in enumerate(lists) if curr], key=lambda x:x[1])[0]
            head.next = lists[idx]
            lists[idx] = lists[idx].next
            head = head.next

        return dummy.next
