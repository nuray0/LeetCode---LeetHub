# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        unique = sorted(set(l))
    
        cur = dummy = ListNode(0)
        for e in unique:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
        