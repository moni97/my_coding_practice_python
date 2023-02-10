class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(numbers)):
            if numbers[i] in res:
                return [res[numbers[i]] + 1, i+1]
            res[target - numbers[i]] = i
        
