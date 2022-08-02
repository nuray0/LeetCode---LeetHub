# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return
        out = []
        self.helper(root, out)
        for i in range(1, len(out)):
            if out[i - 1] >= out[i]:
                return False
        return True
            
    def helper(self, root, out):
        if root:
            self.helper(root.left, out)
            out.append(root.val)
            self.helper(root.right, out)
        