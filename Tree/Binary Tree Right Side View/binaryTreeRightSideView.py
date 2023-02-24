# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        from collections import deque
        res = []
        fifo = deque()
        level = 1
        dictCount = []
        fifo.append((root, level))
        while fifo:
            for i in range(len(fifo)):
                node, currLevel = fifo.popleft()
                if node:
                    if currLevel not in dictCount:
                        res.append(node.val)
                        dictCount.append(currLevel)
                    fifo.append((node.right, currLevel + 1))
                    fifo.append((node.left, currLevel + 1))
        return res
       
