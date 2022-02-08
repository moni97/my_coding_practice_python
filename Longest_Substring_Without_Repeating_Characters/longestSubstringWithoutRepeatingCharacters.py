class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        newString = ''
        for index, char in enumerate(s):
            if char not in newString:
                newString = newString + char
            else:
                newString = newString[newString.index(char) + 1:]
                newString = newString + char
            maxi = max(maxi, len(newString))
        return maxi
