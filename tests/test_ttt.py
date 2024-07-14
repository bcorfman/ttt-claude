import pytest

from core.ttt import generate_tic_tac_toe_states


@pytest.fixture(scope="module")
def states():
    return generate_tic_tac_toe_states()


def test_empty_board(states):
    assert "." * 9 in states


def test_exact_state_count(states):
    expected_count = 5478
    assert len(states) == expected_count


def test_invalid_states(states):
    invalid_states = [
        "XXX......",  # X wins but O hasn't played
        "XXXOO...O",  # X wins but O has equal moves
        "XXXOOO...",  # Both X and O win
        "OOOXX....",  # O wins and went first
        "OOO......",  # O wins and X didn't move
        "XOOXOXOXO",  # O has more moves than X
    ]
    for state in invalid_states:
        assert state not in states


def test_valid_states(states):
    valid_states = [
        "X........",  # X's first move
        "XO.......",  # O's first move
        "XOXOXOXOX",  # Full board, X wins (5 X's, 4 O's)
        "XOXXOOOXX",  # Full board, O wins (5 X's, 4 O's)
        "XOXOOXXXO",  # Full board, draw (5 X's, 4 O's)
    ]
    for state in valid_states:
        assert state in states


def test_x_always_first(states):
    for state in states:
        x_count = state.count("X")
        o_count = state.count("O")
        assert x_count >= o_count
        assert x_count <= o_count + 1


if __name__ == "__main__":
    pytest.main()
