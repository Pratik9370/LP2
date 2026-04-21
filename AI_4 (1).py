# B4: N-Queens using Backtracking (with Branch & Bound optimization)

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Arrays for Branch & Bound
    rows = [False] * n
    diag1 = [False] * (2 * n - 1)   # row + col
    diag2 = [False] * (2 * n - 1)   # row - col + (n-1)

    def solve(col):
        if col >= n:
            return True

        for row in range(n):
            # Check if safe
            if not rows[row] and not diag1[row + col] and not diag2[row - col + n - 1]:

                # Place queen
                board[row][col] = 1
                rows[row] = diag1[row + col] = diag2[row - col + n - 1] = True

                # Recur for next column
                if solve(col + 1):
                    return True

                # Backtrack
                board[row][col] = 0
                rows[row] = diag1[row + col] = diag2[row - col + n - 1] = False

        return False

    if solve(0):
        return board
    else:
        return None


# ----------- Main Program -----------

n = int(input("Enter value of N (number of queens): "))

solution = solve_n_queens(n)

if solution:
    print("\nSolution (1 = Queen, 0 = Empty):")
    for row in solution:
        print(row)
else:
    print("\nNo solution exists")