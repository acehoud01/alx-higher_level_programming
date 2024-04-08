#!/usr/bin/python3
import sys


def print_solution(board):
    """Prints the solution to the N queens problem."""
    solution = []
    for row in board:
        position = [row.index(1), board.index(row)]
        solution.append(position)
    print(solution)


def is_safe(board, row, col, n):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    """Uses backtracking to solve the N Queens problem."""
    if col >= n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens(board, col + 1, n)
            board[i][col] = 0


def nqueens(n):
    """The main function to solve the N Queens problem."""
    board = [[0] * n for _ in range(n)]
    solve_n_queens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
