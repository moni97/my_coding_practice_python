class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {c: 0 for c in string.ascii_lowercase}
        window = {c: 0 for c in string.ascii_lowercase}
        len_s1 = len(s1)
        for c in s1:
            target[c] += 1
        for c in s2[:len_s1]:
            window[c] += 1
        for i in range(len_s1, len(s2)):
            if target == window:
                return True
            window[s2[i-len_s1]] -= 1
            window[s2[i]] += 1
        return window == target
