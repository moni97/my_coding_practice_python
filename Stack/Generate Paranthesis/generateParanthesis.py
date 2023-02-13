class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open1, close, curr):
            if open1 < n:
                curr.append("(")
                backtrack(open1 + 1, close, curr)
                curr.pop()
            if close < n and close < open1:
                curr.append(")")
                backtrack(open1, close + 1, curr)
                curr.pop()
            if open1 == n and close == n:
                res.append("".join(curr))
            return
        backtrack(0, 0, [])
        return res
