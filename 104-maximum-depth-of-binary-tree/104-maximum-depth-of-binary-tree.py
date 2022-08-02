# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max = 0
        level = [root]
        while root and level:
            max += 1
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return max