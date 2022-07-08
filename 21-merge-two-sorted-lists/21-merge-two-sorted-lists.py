# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        ls1 = []
        ls2 = []
        
        while l1:
            ls1.append(l1.val)
            l1 = l1.next
        while l2:
            ls2.append(l2.val)
            l2 = l2.next
        

            
        res = ls1 + ls2
        res.sort()
    
        cur = new_link = ListNode()
        for i in res:
            cur.next = ListNode(i)
            cur = cur.next
            
        return new_link.next
        