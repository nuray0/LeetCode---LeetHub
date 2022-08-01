# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.helper(root, out)
        return out

    def helper(self, root, out):
        if root:
            self.helper(root.left, out)
            self.helper(root.right, out)
            out.append(root.val)  