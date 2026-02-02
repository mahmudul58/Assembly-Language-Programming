import heapq

N = 3
row = [0, 0, -1, 1]
column = [-1, 1, 0, 0]

GOAL_STATE = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

class Board:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth
        self.h = heuristic_value(board)
        self.f = self.depth + self.h

    def __lt__(self, other):
        return self.f < other.f

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    return board == GOAL_STATE

def heuristic_value(board):
    goal_pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,2), 6:(2,0),
        7:(2,1), 8:(2,2)
    }
    distance = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                x, y = goal_pos[val]
                distance += abs(i-x) + abs(j-y)
    return distance

def a_star_search(start, x, y):
    pq = []
    visited = set()

    heapq.heappush(pq, Board(start, x, y, 0))

    while pq:
        current = heapq.heappop(pq)
        board_tuple = tuple(map(tuple, current.board))

        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        print("Depth:", current.depth, "Heuristic:", current.h)
        for r in current.board:
            print(r)
        print()

        if is_goal(current.board):
            print("Solution Found")
            return

        for i in range(4):
            new_x = current.x + row[i]
            new_y = current.y + column[i]

            if is_valid(new_x, new_y):
                new_board = [r[:] for r in current.board]
                new_board[current.x][current.y], new_board[new_x][new_y] = \
                new_board[new_x][new_y], new_board[current.x][current.y]

                heapq.heappush(pq, Board(new_board, new_x, new_y, current.depth + 1))

    print("No Solution")

start_board = [[1,2,3],[5,0,6],[4,7,8]]
a_star_search(start_board, 1, 1)
