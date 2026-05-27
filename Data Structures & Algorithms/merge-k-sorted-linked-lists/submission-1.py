# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        currs = [head for head in lists]
        dummy = ListNode()
        head = dummy
        while any(currs):
            idx = min([(i, curr.val) for i, curr in enumerate(currs) if curr], key=lambda x:x[1])
            head.next = currs[idx[0]]
            currs[idx[0]] = currs[idx[0]].next
            head = head.next

        return dummy.next
