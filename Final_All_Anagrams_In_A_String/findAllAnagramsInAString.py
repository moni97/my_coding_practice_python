def findAnagrams(self, s: str, p: str) -> List[int]:
        p_list, s_list, s_len, p_len = defaultdict(int), defaultdict(int), len(s), len(p)
        left_ptr, right_ptr = 0, p_len - 1
        res = []
        if p_len > s_len:
            return res
        for i in range(0, p_len-1):
            s_list[s[i]] += 1
        for char in p:
            p_list[char] += 1
        while right_ptr < len(s):
            break_flag = False
            s_list[s[right_ptr]] += 1
            for i in p_list.keys():
                if p_list[i] != s_list[i]:
                    break_flag = True
                    break
            if break_flag == False:
                res.append(left_ptr)
            s_list[s[left_ptr]] -= 1
            left_ptr += 1
            right_ptr += 1
        return res
