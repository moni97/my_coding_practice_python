    def partitionLabels(self, s: str) -> List[int]:
        visited = {}
        res = []
        boundry = s[0]
        last_index = 0
        for i in range(0, len(s)):
            if s[i] in visited:
                start, end = visited[s[i]]
                visited[s[i]] = (start, i)
            else:
                visited[s[i]] = (i, i)
        currStart, currEnd = visited[s[0]]
        wordToInclude = set()
        res = []
        _len = 1
        max_end = currEnd
        i = 1
        for i in range(1, len(s)):
            if i <= currEnd or i < max_end:
                wordToInclude.add(s[i])
                max_end = max(max_end, visited[s[i]][1])
                _len += 1
            elif i > currEnd:
                if s[i] not in wordToInclude:
                    res.append(_len)
                    wordToInclude.clear()
                    wordToInclude.add(s[i])
                    currStart, currEnd = visited[s[i]]
                    _len = 1
                else:
                    _len += 1
            if i == len(s) - 1:
                res.append(_len)
        return res
