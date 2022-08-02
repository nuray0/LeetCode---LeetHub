# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, out):
        if root is None:
            return     
        self.helper(root.left, out)
        out.append(root.val)
        self.helper(root.right, out)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        out = []
        self.helper(root, out)
        length = len(out)
        for i in range(1, length):
            if out[i - 1] >= out[i]:
                return False
        return True
        