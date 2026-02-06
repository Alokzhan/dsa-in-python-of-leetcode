class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for char in "123456789":
                        if self.is_valid(board, r, c, char):
                            board[r][c] = char
                            
                            # If this choice leads to a solution, return True
                            if self.solve(board):
                                return True
                            
                            # Backtrack: if not, undo the choice
                            board[r][c] = "."
                    
                    # If no number 1-9 works, this path is invalid
                    return False
        return True

    def is_valid(self, board, r, c, char):
        # Check row, column, and 3x3 box simultaneously
        for i in range(9):
            # Check row
            if board[r][i] == char:
                return False
            # Check column
            if board[i][c] == char:
                return False
            # Check 3x3 box
            # (r // 3) * 3 gives the start row of the box
            # (c // 3) * 3 gives the start col of the box
            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == char:
                return False
        return True
