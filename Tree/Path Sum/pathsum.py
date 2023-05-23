# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node: return False
            if node.left == None and node.right == None:
                if currSum + node.val == targetSum: return True
                else: return False
            leftRes = dfs(node.left, currSum + node.val)
            rightRes = dfs(node.right, currSum + node.val)
            if leftRes: return leftRes
            if rightRes: return rightRes
            return False
        if root == None:
            return False
        return dfs(root, 0)
