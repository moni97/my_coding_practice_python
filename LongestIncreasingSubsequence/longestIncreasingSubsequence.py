def lengthOfLIS(self, nums: List[int]) -> int:
        len_nums = len(nums)
        dp = [1] * (len_nums)
        for i in range(len_nums-2, -1, -1):
            for j in range(i+1, len_nums):
                if nums[i] < nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
