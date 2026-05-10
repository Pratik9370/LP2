import heapq

def is_safe(board, row, col):
    for c, r in enumerate(board):
        if r == row or abs(r - row) == abs(c - col):
            return False
    return True

def solve_4_queens():
    # Priority Queue: (cost_to_goal, current_col, board_state)
    # cost_to_goal: 4 minus number of queens placed
    pq = [(4, 0, [])]

    while pq:
        cost, col, board = heapq.heappop(pq)

        if col == 4:
            print_board(board)
            continue # Search for more solutions

        for row in range(4):
            if is_safe(board, row, col):
                new_board = board + [row]
                # Priority = total queens needed (4) - queens already placed
                priority = 4 - len(new_board)
                heapq.heappush(pq, (priority, col + 1, new_board))

def print_board(board):
    for r in range(4):
        print(" ".join("Q" if board[c] == r else "." for c in range(4)))
    print("-" * 7)

solve_4_queens()