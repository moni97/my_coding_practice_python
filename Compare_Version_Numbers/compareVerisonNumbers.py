class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_split = version1.split('.')
        version2_split = version2.split('.')
        max_len = max(len(version1_split), len(version2_split))
        for i in range(max_len): 
            str1 = version1_split[i] if i < len(version1_split) else '0'
            str2 = version2_split[i] if i < len(version2_split) else '0'
            if int(str1) > int(str2):
                return 1
            elif int(str1) < int(str2):
                return -1
        return 0
