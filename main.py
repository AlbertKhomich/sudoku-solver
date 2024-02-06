file_path = './text.txt'
with open(file_path, 'r') as file:
    sudoku = file.readlines()
lines = [list(line.strip()) for line in sudoku]


def find_border(coord):
    if coord <= 2:
        border = 2
    elif coord <= 5:
        border = 5
    else:
        border = 8
    return border


def check(x, y, number):
    square = []
    x_direction = [number for number in lines[y]]
    y_direction = list(list(zip(*lines))[x])

    x_border = find_border(x)
    y_border = find_border(y)
    for y in range(y_border - 2, y_border + 1):
        square.extend(list(lines[y][x_border - 2: x_border + 1]))

    return True if number not in square + x_direction + y_direction else False


def find_empty(puzzle):
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == '0':
                return x, y


def solve(puzzle):
    empty = find_empty(puzzle)
    if not empty:
        return True
    x, y = empty

    for option in range(1, 10):
        if check(x, y, str(option)):
            puzzle[y][x] = str(option)
            if solve(puzzle):
                return True
            puzzle[y][x] = '0'

    return False


solve(lines)

count = 0
for i, line in enumerate(lines):
    count += 1
    print(''.join(line[0:3]), ''.join(line[3:6]), ''.join(line[6:9]))
    if count % 3 == 0:
        print()












