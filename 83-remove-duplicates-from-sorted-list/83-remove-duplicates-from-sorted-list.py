# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # checking next value and skipping it if equal to current value
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head
        
        # turning ll into list, sorting it's set 
        # and creating a new ll from the list
        # could be the decision if ll wasn't sorted
#        l = []
#        while head:
#            l.append(head.val)
#            head = head.next
#        unique = sorted(set(l))  
#        cur = dummy = ListNode(0)
#        for e in unique:
#            cur.next = ListNode(e)
#            cur = cur.next
#        return dummy.next
        