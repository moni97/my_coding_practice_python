class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for i in range((n//2) + 1):
            if i != 0:
                res.append(i)
                res.append(-1 * i)
            elif n % 2 == 1:
                res.append(0)
        return res
