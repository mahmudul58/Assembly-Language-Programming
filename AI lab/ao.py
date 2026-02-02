N = 3
row = [0, 0, -1, 1]
column = [-1, 1, 0, 0]

GOAL_STATE = [[1,2,3],[4,0,5],[6,7,8]]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    return board == GOAL_STATE

def heuristic_value(board):
    goal_pos = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,2),6:(2,0),
        7:(2,1),8:(2,2)
    }
    h = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                x,y = goal_pos[board[i][j]]
                h += abs(i-x) + abs(j-y)
    return h

def ao_star(board, x, y, visited):
    if is_goal(board):
        print("Goal Reached")
        return True

    visited.add(tuple(map(tuple, board)))

    children = []

    for i in range(4):
        new_x = x + row[i]
        new_y = y + column[i]

        if is_valid(new_x, new_y):
            new_board = [r[:] for r in board]
            new_board[x][y], new_board[new_x][new_y] = \
            new_board[new_x][new_y], new_board[x][y]

            if tuple(map(tuple, new_board)) not in visited:
                children.append((heuristic_value(new_board), new_board, new_x, new_y))

    children.sort()

    for _, child, cx, cy in children:
        print("Exploring:")
        for r in child:
            print(r)
        print()
        if ao_star(child, cx, cy, visited):
            return True

    return False

start_board = [[1,2,3],[5,0,6],[4,7,8]]
ao_star(start_board, 1, 1, set())
