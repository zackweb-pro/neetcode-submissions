class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = defaultdict(set)
        for i in range(len(board)):
            r = []
            c = []
            for j in range(len(board)):
               
                if(board[i][j] in r and board[i][j] != '.'):
                    return False
                else:
                    r.append(board[i][j])
                if(board[j][i] in c and board[j][i] != '.'):
                    return False
                else:
                    c.append(board[j][i])
                if board[i][j] in s[(i//3,j//3)] and board[i][j] != '.': 
                    return False
                else:
                    s[(i//3,j//3)].add(board[i][j])
        return True