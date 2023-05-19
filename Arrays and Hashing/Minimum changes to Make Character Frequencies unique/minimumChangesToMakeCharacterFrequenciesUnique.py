class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for c in s:
            if c not in freq: freq[c] = 1 
            else: freq[c] += 1
        values = sorted(list(freq.values()))
        occured = set()
        res = 0
        for item in values:
            if item in occured:
                tmp = item
                while tmp in occured:
                    tmp -= 1
                    res += 1
                if tmp != 0:
                    occured.add(tmp)
            else:
                occured.add(item)
        return res
