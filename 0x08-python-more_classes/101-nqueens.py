#!/usr/bin/python3
import sys


def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe (no conflicts).
  """
  for i in range(col):
    if board[row][i] == 'Q':
      return False
  
  i, j = row, col
  while i >= 0 and j >= 0:
    if board[i][j] == 'Q':
      return False
    i -= 1
    j -= 1
  
  i, j = row, col
  while i >= 0 and j < len(board):
    if board[i][j] == 'Q':
      return False
    i -= 1
    j += 1
  
  return True


def solve_n_queens(board, col):
  """
  Solves the N queens problem recursively.
  """
  if col >= len(board):
    for row in board:
      print(''.join(row))
    return
  
  for i in range(len(board)):
    if is_safe(board, i, col):
      board[i][col] = 'Q'
      solve_n_queens(board, col + 1)
      board[i][col] = '.'

def main():
  if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)
  
  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)
  
  if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)
  
  board = [['.' for _ in range(n)] for _ in range(n)]
  
  solve_n_queens(board, 0)

if __name__ == "__main__":
  main()

