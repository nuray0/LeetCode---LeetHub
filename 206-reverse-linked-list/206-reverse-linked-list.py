# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev_node = None
        output = head
        
        while output:
            next_node = output.next
            output.next = prev_node
            prev_node = output
            output = next_node
            
        return prev_node
            