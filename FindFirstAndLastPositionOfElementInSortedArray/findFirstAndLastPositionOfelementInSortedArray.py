def searchRange(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        if len_nums == 0:
            return [-1, -1]
        if len_nums >= 1 and (nums[0] > target or nums[len_nums - 1] < target):
            return [-1, -1]
        first = -1
        last = -1
        i = 0
        while i < len_nums and nums[i] <= target:
            if nums[i] == target:
                if first == -1:
                    first = i
                    last = i
                else: last = i
            i += 1
        return [first, last]
