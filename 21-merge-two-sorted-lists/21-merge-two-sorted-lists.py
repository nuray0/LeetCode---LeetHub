# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = output = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                output.next = list1
                list1 = list1.next
            else:
                output.next = list2
                list2 = list2.next
            output = output.next

        output.next = list1 or list2

        return head.next
    
    
        # copy values into lists, add them and sort, then make a linked list      
#        ls1 = []
#        ls2 = []
#
#        while l1:
#            ls1.append(l1.val)
#            l1 = l1.next
#        while l2:
#            ls2.append(l2.val)
#            l2 = l2.next
#
#        res = ls1 + ls2
#        res.sort()
#    
#        cur = new_link = ListNode()
#        for i in res:
#            cur.next = ListNode(i)
#            cur = cur.next
#            
#        return new_link.next
    

    
