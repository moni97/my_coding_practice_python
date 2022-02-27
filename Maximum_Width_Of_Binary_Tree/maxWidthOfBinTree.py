class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1, 0)]
        prev_level = 1
        min_pos = 0
        maxCount = 0
        while stack:
            node, level, pos = stack.pop(0)
            if level > prev_level:
                prev_level, min_pos = level, pos
            if node:
                if node.left: stack.append((node.left, level + 1, pos * 2))
                if node.right: stack.append((node.right, level + 1, (pos * 2) + 1))     
            maxCount = max(maxCount,  (pos - min_pos) + 1)
        return maxCount
