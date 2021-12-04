data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]

sequence = [int(x) for x in data[0].split(",")]

boards = []
buf = []
for i, ln in enumerate(data):
    if i < 2: continue
    if not ln.strip():
        boards.append(buf)
        buf = []
    else:
        buf.append([int(x) for x in ln.split(" ") if x != ''])
if buf: boards.append(buf)

def check_board(board):
    # rows
    for r in board:
        if sum(r) == -5: return True
    # cols
    columns = list(zip(*board))[::-1]
    for c in columns:
        if sum(c) == -5: return True
    return False

def calculate_board(board):
    sm = 0
    for r in board:
        for c in r:
            if c != -1: sm += c
    return sm

def solve():
    solved = [1]*len(boards)
    for n in sequence:
        for i ,b in enumerate(boards):
            for y, r in enumerate(b):
                for x, c in enumerate(r):
                    if c == n: b[y][x] = -1
                    if check_board(b): solved[i] = 0
                    if sum(solved) == 0: return calculate_board(b) * n

print(solve())
