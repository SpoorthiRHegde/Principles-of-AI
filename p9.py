# Matrix Input
Row = int(input("Enter the number of rows: "))
Column = int(input("Enter the number of columns: "))
matrix = []

print("Enter the entries row-wise:")
for row in range(Row):
    a = []
    for column in range(Column):
        a.append(int(input()))
    matrix.append(a)

print("The matrix is:")
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()

# Tic-Tac-Toe Game
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter col (0, 1, 2): "))
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
