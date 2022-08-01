# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''Iterative approach'''
#    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#        stack, result = [], []
#        while stack or root:
#            if root:
#                stack.append(root)
#                root = root.left
#            else:
#                node = stack.pop()
#                result.append(node.val)
#                root = node.right
#        return result
    
    '''Recursive approach'''
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.helper(root, out)
        return out
    
    def helper(self, root, out):
        if (root == None):
            return
        else:
            self.helper(root.left, out)
            out.append(root.val)
            self.helper(root.right, out)
 
 