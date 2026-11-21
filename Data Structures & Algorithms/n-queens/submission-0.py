class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        PosDia = set()
        NegDia = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
            
            for c in range(n):
                if c in col or (r + c) in PosDia or (r - c) in NegDia:
                    continue
                
                col.add(c)
                PosDia.add(r + c)
                NegDia.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                PosDia.remove(r + c)
                NegDia.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)
        return res
