def findMin(self, nums: List[int]) -> int:
        ptr = 1
        nums_len = len(nums)
        while ptr < nums_len and nums[ptr-1] < nums[ptr]:
            ptr += 1
        return nums[ptr] if ptr != nums_len else nums[0]
