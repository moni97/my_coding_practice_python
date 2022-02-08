class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.numberToLetter = {}
        self.numberToLetter['2'] = ['a', 'b', 'c']
        self.numberToLetter['3'] = ['d', 'e', 'f']
        self.numberToLetter['4'] = ['g', 'h', 'i']
        self.numberToLetter['5'] = ['j', 'k', 'l']
        self.numberToLetter['6'] = ['m', 'n', 'o']
        self.numberToLetter['7'] = ['p', 'q', 'r', 's']
        self.numberToLetter['8'] = ['t', 'u', 'v']
        self.numberToLetter['9'] = ['w', 'x', 'y', 'z']
        res = []
        def getCombination(index1, combo):
            if len(combo) == len(digits):
                res.append(combo) 
                return
            for c in self.numberToLetter[digits[index1]]:
                getCombination(index1 + 1, combo + c)
        
        if digits:
            getCombination(0, '')
            return res
