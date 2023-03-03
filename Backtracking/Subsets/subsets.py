def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        def traverse(i, curr):
            final.append(curr.copy())
            for j in range(i, len(nums)):
                curr.append(nums[j])
                traverse(j + 1, curr)
                curr.pop()
        
        traverse(0, [])
        return final
