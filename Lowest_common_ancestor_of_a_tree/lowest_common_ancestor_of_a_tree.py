if not node:
            return None
        res_left = self.lowestCommonAncestor(node.left, p, q) if node.left else None
        res_right = self.lowestCommonAncestor(node.right, p, q) if node.right else None
        if res_left and res_right:
            return node
        if node.val == p.val or node.val == q.val:
            if res_right or res_left:
                return node
            return True
        if res_left:
            return res_left
        elif res_right:
            return res_right
        else:
            return False
        return node
