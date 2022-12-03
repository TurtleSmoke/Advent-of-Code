import numpy as np

with open('input', 'r') as f:
    dots, fold = f.read().split("\n\n")

dots = np.array(([[int(x) for x in dot.split(',')]
                  for dot in dots.splitlines()]))
fold = [f.split('fold along ')[1].split('=') for f in fold.split("\n")]

board = np.full((max(dots[:, 1]) + 1, max(dots[:, 0]) + 1), False)

for x, y in dots:
    board[y, x] = 1

for d, v in fold[:1]:
    v = int(v)
    flip = board[:, v + 1:] if d == 'x' else board[v + 1:, :]
    flip = np.flip(flip, 1 if d == 'x' else 0)
    board = np.logical_or(board[:, :v] if d == 'x' else board[:v, :], flip)

print(np.sum(board))

for d, v in fold[1:]:
    v = int(v)
    flip = board[:, v + 1:] if d == 'x' else board[v + 1:, :]
    flip = np.flip(flip, 1 if d == 'x' else 0)
    board = np.logical_or(board[:, :v] if d == 'x' else board[:v, :], flip)

board = np.array([['#' if x else '.' for x in line] for line in board])
print('\n'.join(''.join(x for x in line) for line in board))

