class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch( 0, len(nums) - 1, True, target, nums)
        right = self.binSearch( 0, len(nums) - 1, False, target, nums)
        return [left, right]
        
    def binSearch(self, l, r, leftBias, target, nums):
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
