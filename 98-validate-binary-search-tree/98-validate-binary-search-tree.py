# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        out = []
        self.helper(root, out)
        return out == sorted(set(out))
            
    def helper(self, root, out):
        if root:
            self.helper(root.left, out)
            out.append(root.val)
            self.helper(root.right, out)
        