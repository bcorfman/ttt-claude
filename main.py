from core.ttt import generate_tic_tac_toe_states

if __name__ == "__main__":
    # Generate and count the states
    states = generate_tic_tac_toe_states()
    state_count = len(states)

    print(f"Total number of valid tic-tac-toe game states: {state_count}")
