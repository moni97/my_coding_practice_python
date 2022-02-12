 def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def getInorder(node, res):
            stack = []
            while stack or node:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                res.append(node.val)
                node = node.right
            return res
        inorder1 = getInorder(root1, [])
        inorder2 = getInorder(root2, [])
        res = []
        ptr1, ptr2 = 0, 0
        while ptr1 < len(inorder1) and ptr2 < len(inorder2):
            if inorder1[ptr1] <= inorder2[ptr2]:
                res.append(inorder1[ptr1])
                ptr1 += 1
            elif inorder1[ptr1] > inorder2[ptr2]:
                res.append(inorder2[ptr2])
                ptr2 += 1
        while ptr1 < len(inorder1):
            res.append(inorder1[ptr1])
            ptr1 += 1
        while ptr2 < len(inorder2):
            res.append(inorder2[ptr2])
            ptr2 += 1
        return res
