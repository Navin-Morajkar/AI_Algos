def feasible(board, row, col, n):
    for c in range(col):
        if board[row][c] == 1:
            return False

    for r in range(n):
        if board[r][col] == 1:
            return False

    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    return True


def placement(n):
    board = [[0] * n for _ in range(n)]
    col = 0

    while col < n:
        while True:
            pos_input = input(f"Enter the (column, row) coordinates to place the queen: ")
            pos = pos_input.split(",")
            if len(pos) != 2:
                print("Invalid input! Please enter the coordinates in the format 'column,row'.")
                continue

            try:
                col_input = int(pos[0].strip()) - 1
                row_input = int(pos[1].strip()) - 1
            except ValueError:
                print("Invalid input! Please enter valid integer values for the coordinates.")
                continue

            if col_input < 0 or col_input >= n or row_input < 0 or row_input >= n:
                print(f"Invalid position! Please enter values between 1 and {n}.")
                continue

            if not feasible(board, row_input, col_input, n):
                print("Constraint Violation! Please select a different position.")
                continue

            board[row_input][col_input] = 1
            break

        col += 1

    print("\nSolution:")
    for row in board:
        print(' '.join(str(cell) for cell in row))


if __name__ == "__main__":
    while True:
        n = int(input("Enter the number of queens: "))
        if n <= 0:
            print("Invalid input. Please enter a positive number.")
            continue

        placement(n)

        choice = input("Do you wish to restart? (yes/no): ")
        if choice.lower() == "no":
            break
