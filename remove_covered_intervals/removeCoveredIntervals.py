def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        len_int = len(intervals)
        if len_int == 1:
            return len_int
        intervals = sorted(intervals)
        res = [intervals[0]]
        for i in range(1, len_int):
            prev = res[-1]
            if intervals[i][0] == prev[0] and intervals[i][1] > prev[1] or intervals[i][0] > prev[0] and intervals[i][1] == prev[1]:
                res.pop()
                res.append(intervals[i])
            elif intervals[i][0] > prev[0] and intervals[i][1] > prev[1]:
                res.append(intervals[i])
        return len(res)
