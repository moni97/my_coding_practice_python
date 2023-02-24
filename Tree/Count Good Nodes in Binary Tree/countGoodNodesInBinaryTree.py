# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        good = 0
        def dfs(node, maxVal):
            if not node:
                return 0
            res = 0
            maxVal = max(node.val, maxVal)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            if node.val >= maxVal:
                return 1 + res
            else:
                return res
        good = dfs(root, root.val)
        return good
