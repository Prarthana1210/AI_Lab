def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):

    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def board_full(board):
    for row in board:
        if ' ' in row:
            return False

    return True


def get_move(board, player):

    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid input! Enter numbers between 0 and 2.")
                continue

            if board[row][col] != ' ':
                print("Cell already occupied! Try again.")
                continue

            return row, col

        except ValueError:
            print("Invalid input! Please enter numbers.")


def play():

    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]

    player = 'X'

    while True:

        print_board(board)

        row, col = get_move(board, player)

        board[row][col] = player

        # Check winner
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Check draw
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'


if __name__ == "__main__":
    play()