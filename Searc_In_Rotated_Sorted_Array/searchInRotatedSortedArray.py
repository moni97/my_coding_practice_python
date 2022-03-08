def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return 0 if nums[0] == target else -1
        i = 1
        left, right = 0, 0
        while i < nums_len and nums[i-1] < nums[i]:
            i += 1
        if target == nums[i-1]:
            return i-1
        elif target >= nums[0] and target <= nums[i-1]:
            left = 0
            right = i - 1
        elif i < nums_len and target >= nums[i] and target <= nums[nums_len - 1]:
            left = i
            right = nums_len - 1
        else:
            return -1
        while left <= right:
            if left == right:
                if nums[left] == target:
                    return left
                else: return -1
            mid = (left + (right - 1)) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1
