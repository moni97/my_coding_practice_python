class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            return point[0] ** 2 + point[1] ** 2
        distDict = [(distance(p), p[0], p[1]) for p in points]
        heapq.heapify(distDict)
        res = []
        if len(distDict) < k:
            return points
        else:
            for i in range(k):
                _, x, y = heapq.heappop(distDict)
                res.append([x, y])
            return res
