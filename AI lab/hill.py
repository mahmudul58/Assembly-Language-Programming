N = 3
row = [0, 0, -1, 1]
column = [-1, 1, 0, 0]

GOAL_STATE = [[1,2,3],[4,0,5],[6,7,8]]

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

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def hill_climbing(start, x, y):
    current = start
    curr_h = heuristic_value(current)

    while True:
        print("Heuristic:", curr_h)
        for r in current:
            print(r)
        print()

        if current == GOAL_STATE:
            print("Goal Reached")
            return

        neighbors = []

        for i in range(4):
            new_x = x + row[i]
            new_y = y + column[i]

            if is_valid(new_x, new_y):
                new_board = [r[:] for r in current]
                new_board[x][y], new_board[new_x][new_y] = \
                new_board[new_x][new_y], new_board[x][y]

                neighbors.append((heuristic_value(new_board), new_board, new_x, new_y))

        neighbors.sort()
        best_h, best_board, bx, by = neighbors[0]

        if best_h >= curr_h:
            print("Stuck at Local Maximum")
            return

        current, curr_h, x, y = best_board, best_h, bx, by

start_board = [[1,2,3],[5,0,6],[4,7,8]]
hill_climbing(start_board, 1, 1)
