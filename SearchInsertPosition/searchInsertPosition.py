def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right + 1) // 2
            # print('mid: ', mid, 'nums[mid]: ', nums[mid], 'l: ', left, 'r: ', right) 
            if target == nums[mid]: return mid
            if left == right:
                if target < nums[left]: return left
                elif target > nums[right]: return right + 1
            if target < nums[mid]: right = mid - 1
            elif target > nums[mid]: left = mid + 1
        return left
