from itertools import product


def generate_tic_tac_toe_states():
    empty = "."
    players = ["X", "O"]
    states = set()

    def is_valid_state(board):
        x_count = board.count("X")
        o_count = board.count("O")
        if x_count < o_count or x_count > o_count + 1:
            return False
        if has_winner(board, "X") and has_winner(board, "O"):
            return False
        if has_winner(board, "X") and x_count <= o_count:
            return False
        if has_winner(board, "O") and x_count != o_count:
            return False
        return True

    def has_winner(board, player):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),  # Rows
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),  # Columns
            (0, 4, 8),
            (2, 4, 6),  # Diagonals
        ]
        return any(
            all(board[i] == player for i in combo) for combo in winning_combinations
        )

    for moves in product(players + [empty], repeat=9):
        board = "".join(moves)
        if is_valid_state(board):
            states.add(board)

    return states
