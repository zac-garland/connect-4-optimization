import random
from typing import List, Optional
from .utils import validate_board, legal_moves

def predict_move(
    board: List[List[int]],
    model_type: str = "cnn",
    player: int = 1
) -> Optional[int]:
    """
    Phase 1 dummy predictor:
    - Always returns a LEGAL move (0–6)
    - Prefers center column if available
    - Ignores model_type and player for now
    """

    validate_board(board)
    moves = legal_moves(board)

    if not moves:
        return None

    # Center preference (strong Connect-4 heuristic)
    if 3 in moves:
        return 3

    return random.choice(moves)
	