N = 3

class Board:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth

row = [0, 0, -1, 1]
column = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    goal = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    return goal == board

def dfs(start, x, y):
    stack = []
    visited = set()

    stack.append(Board(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    while stack:
        current = stack.pop()
        print(f"Depth: {current.depth}")
        for r in current.board:
            print(r)
        print()

        if is_goal(current.board):
            print("Solution found at depth:", current.depth)
            return

        for i in range(4):
            new_x = current.x + row[i]
            new_y = current.y + column[i]

            if is_valid(new_x, new_y):
                new_board = [r[:] for r in current.board]
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                    new_board[new_x][new_y], new_board[current.x][current.y]

                board_tuple = tuple(map(tuple, new_board))
                if board_tuple not in visited:
                    visited.add(board_tuple)
                    stack.append(Board(new_board, new_x, new_y, current.depth + 1))

    print("No solution found.")

start_board = [
    [1, 2, 3],
    [5, 0, 6],
    [4, 7, 8]
]
x = 1
y = 1

dfs(start_board, x, y)
