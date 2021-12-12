with open('input', 'r') as file:
    values = [line for line in file.read().splitlines()]

numbers = values[0].split(',')
boards = [[[(x, False) for x in v.split()] for v in values[i:i + 5]] for i in
          range(2, len(values), 6)]

winner = lambda boards: any(
    any(all(v[1] for v in line) for line in board) for board in
    [boards, zip(*boards)])

update = lambda board, x: [[(v[0], True) if v[0] == x else v for v in line] for
                           line in board]

save = boards
for n in numbers:
    boards = [update(board, n) for board in boards]
    for board in boards:
        if winner(board):
            print(int(n) * sum(
                sum(int(v[0]) if not v[1] else 0 for v in line) for line in
                board))
            break
    else:
        continue
    break

boards = save
for n in numbers:
    boards = [update(board, n) for board in boards]
    if len(boards) == 1:
        if winner(boards[0]):
            print(int(n) * sum(
                sum(int(v[0]) if not v[1] else 0 for v in line) for line in
                boards[0]))
            break
    boards = [board for board in boards if not winner(board)]
