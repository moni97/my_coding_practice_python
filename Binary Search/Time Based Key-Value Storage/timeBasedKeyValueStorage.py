class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        val = self.map.get(key,[])
        res = ""
        l, r = 0, len(val) - 1
        while l <= r:
            mid = (l + r) // 2
            curr = val[mid]
            if curr[1] <= timestamp:
                res = curr[0]
                l = mid + 1
            elif curr[1] > timestamp:
                r = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
