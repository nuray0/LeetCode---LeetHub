# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:     
    def hasPathSum(self, root, sum):
        stack = [(root, sum)]
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right and node.val == value:
                    return True
                stack.append((node.right, value-node.val))
                stack.append((node.left, value-node.val))
        return False