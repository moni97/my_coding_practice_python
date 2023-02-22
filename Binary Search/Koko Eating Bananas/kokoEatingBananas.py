class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l + r) // 2
            totalH = 0
            for val in piles:
                totalH += math.ceil(val/k)
            if totalH <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res
        
        
