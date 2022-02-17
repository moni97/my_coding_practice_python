def exist(self, board: List[List[str]], word: str) -> bool:
        row, col, word_len = len(board), len(board[0]), len(word)
        # Adding the following for loop in my code reduced the time limit from 7340ms to 2499ms
        for letter in tuple(set(word)):
            if flat.count(letter) < word.count(letter):
                return False
        def dfs(pos, index):
            if index == word_len:
                return True
            if  pos[0] < 0 or pos[0] >= row or col <= pos[1] or pos[1] < 0 or index > word_len:
                return False
            if board[pos[0]][pos[1]] != word[index]:
                return False
            tmp = board[pos[0]][pos[1]]
            board[pos[0]][pos[1]] = '#'
            res = dfs((pos[0] + 1, pos[1]), index+1) or dfs((pos[0] - 1, pos[1]), index+1) or dfs((pos[0], pos[1] + 1), index + 1) or dfs((pos[0], pos[1] - 1), index + 1)
            board[pos[0]][pos[1]] = tmp
            return res     
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs((i, j), 0):
                    return True
        return False
