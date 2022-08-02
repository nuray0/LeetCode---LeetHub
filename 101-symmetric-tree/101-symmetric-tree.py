# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def symmetric(a, b):
            if a is None and b is None:
                return True
            elif a is None or b is None:
                return False
            else:
                return (a.val == b.val and \
                       symmetric(a.left, b.right) and \
                       symmetric(a.right, b.left))
    
        return symmetric(root.left, root.right)
            
        