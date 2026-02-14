class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        # Tracking sets for O(1) lookups
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        def backtrack(r):
            if r == n:
                # Found a valid configuration
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # "Choose" - Place the queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # "Explore" - Move to the next row
                backtrack(r + 1)

                # "Unchoose" - Remove the queen (Backtrack)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
