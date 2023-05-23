def maxLength(self, arr: List[str]) -> int:
        charSet = set()
        def backtrack(i):
            if i == len(arr):
                return len(charSet)
            res = 0
            c = Counter(arr[i]) + Counter(charSet)
            if not max(c.values()) > 1:
                for c in arr[i]:
                    charSet.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charSet.remove(c)
            return max(res, backtrack(i+1))
        return backtrack(0)
