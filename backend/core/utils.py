from typing import List

def validate_board(board: List[List[int]]) -> None:
    if len(board) != 6:
        raise ValueError("Board must have 6 rows")

    for row in board:
        if len(row) != 7:
            raise ValueError("Each row must have 7 columns")
        for cell in row:
            if cell not in (-1, 0, 1):
                raise ValueError("Board values must be -1, 0, or 1")

def legal_moves(board: List[List[int]]) -> List[int]:
    """
    A column is legal if the top cell (row 0) is empty.
    """
    return [col for col in range(7) if board[0][col] == 0]
