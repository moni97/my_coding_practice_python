class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums2 = [-1 * n for n in stones]
        heapq.heapify(nums2)
        # print(nums2)
        while len(nums2) >1:
            x = heapq.heappop(nums2)
            y = heapq.heappop(nums2)
            if y > x:
                heapq.heappush(nums2, x - y)
        return -1 * nums2[0] if len(nums2) > 0 else 0
