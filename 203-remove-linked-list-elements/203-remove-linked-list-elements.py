# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        output = ListNode(-1)
        output.next = head
        
        cur = output
        
        while cur.next != None:
            if cur.next.val == val:
                cur.next = cur.next.next if cur.next.next else None
            else:
                cur = cur.next
                    
        return output.next
        