def print_board(board: list[str]) -> None:
    print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("   |   |")


def check_win(board: list[str], player: str) -> bool:
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for positions in win_positions:
        if all(board[pos] == player for pos in positions):
            return True
    return False


def tic_tac_toe() -> None:
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]
    while True:
        print_board(board)
        print(f"It's {current_player}'s turn.")
        choice = input("Enter a position (1-9): ")
        if not choice.isdigit() or int(choice) not in range(1, 10):
            print("Invalid choice. Try again.")
            continue
        position = int(choice) - 1
        if board[position] != " ":
            print("That position is already taken. Try again.")
            continue
        board[position] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(current_player + " wins!")
            break
        if " " not in board:
            print_board(board)
            print("It's a tie!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]


if __name__ == "__main__":
    tic_tac_toe()
