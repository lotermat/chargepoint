import copy
import pprint

# Returns future of `board`, after `tick` number of ticks
def run_life(board, tick=10):
    new_board = one_tick(board)
    #pprint.pprint(new_board)
    for i in range(1, tick):
        new_board = one_tick(new_board)
        #pprint.pprint(new_board)
    return new_board


# Returns next tick for existing board        
def one_tick(board):
    new_board = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[i][j] = one_cell(board, i, j)
    return new_board


# Based on existing board, returns decision for cell [x][y] in next board
def one_cell(board, x, y):
    neighbor_count = 0
    if x > 0 and y > 0 and board[x-1][y-1]:
        neighbor_count += 1
    if x > 0 and board[x-1][y]:
        neighbor_count += 1
    if x > 0 and y + 1 < len(board[x]) and board[x-1][y+1]:
        neighbor_count += 1
    if y > 0 and board[x][y-1]:
        neighbor_count += 1
    if y + 1 < len(board[x]) and board[x][y+1]:
        neighbor_count += 1
    if x + 1 < len(board) and y > 0 and board[x+1][y-1]:
        neighbor_count += 1
    if x + 1 < len(board) and board[x+1][y]:
        neighbor_count += 1
    if x + 1 < len(board) and y + 1 < len(board[x]) and board[x+1][y+1]:
        neighbor_count += 1

    decision = 0
    if neighbor_count == 2:
        decision = board[x][y]
    elif neighbor_count == 3:
        decision = 1
    #print(board[x][y], neighbor_count, decision)
    return decision


if __name__ == "__main__":
    default = [ [0] * 25 for i in range(25)]

    default[3][1] = 1
    default[4][2] = 1
    default[2][3] = 1
    default[3][3] = 1
    default[4][3] = 1
    pprint.pprint(default)

    pprint.pprint(run_life(default, 10))


