def reverseWords(self, s: str) -> str:
        res = ""
        word = ""
        i = 0
        while i < len(s):
            if not s[i].isspace():
                word += s[i]
            elif word != "":
                res = word if res == "" else word + " " + res
                word = ""
            i += 1
        if word != "":
            res = word + (" " if res else "") + res
        return res
