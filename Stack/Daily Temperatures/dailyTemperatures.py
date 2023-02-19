class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                curr_t, curr_i = stack.pop()
                ans[curr_i] = i - curr_i
            stack.append((t, i))
        return ans
