# #clean
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
# for row in picture:
#     for pixel in row:
#         if pixel == 1:
#             print("*", end="")
#         else:
#             print(" ",end="")
#     print("")
# 
# 
# 
# 
# 
# 
# 
board = [
        [0,3,0,1,0,3,0,1,0,3,0],
        [2,2,2,1,2,2,2,1,2,2,2],
        [0,3,0,1,0,3,0,1,0,3,0],
        [2,2,2,1,2,2,2,1,2,2,2],
        [0,3,0,1,0,3,0,1,0,3,0]
    ]
def display_board(board):
    for row in board:
        for pixel in row:
            if pixel == 1:
                print("|", end="")
            elif pixel == 2:
                print("-", end="")
            elif pixel == 3:
                print(" ",end="")
            elif pixel == "X" or pixel == "O":
                print(pixel, end="")
            else:
                print(" ",end="")
        print("") 


def player_input(player, board):
    while True:
        step_r = int(input("row?0,2,4"))
        step_c = int(input("column? - 1,5,9"))
        if (step_r < 0 or step_r >= len(board) or step_c < 0 or step_c >= len(board[0]) or board[step_r][step_c] != 3):
            print("Try again")
            continue
        board[step_r][step_c] = player
        break
def check_win(board, player):
    if ((board[0][1] == board[0][5] == board[0][9] == player) or
        (board[2][1] == board[2][5] == board[2][9] == player) or
        (board[4][1] == board[4][5] == board[4][9] == player) or
        (board[0][1] == board[2][1] == board[4][1] == player) or
        (board[0][5] == board[2][5] == board[4][5] == player) or
        (board[0][9] == board[2][9] == board[4][9] == player) or
        (board[0][1] == board[2][5] == board[4][9] == player) or
        (board[0][9] == board[2][5] == board[4][1] == player)):
        print(f"{player} WIN!!")
        return True
    return False
def check_draw(board):
    for row in board:
        if 3 in row:
            return False
    return True
def game():
    cur_player = "X"
    for _ in range(9):
        display_board(board)
        player_input(cur_player, board)
        if check_win(board, cur_player):
            break
        if check_draw(board):
            print("DRAW!")
            break
        if cur_player == "X":
            cur_player = "O"
        else:
            cur_player = "X"
    display_board(board)
    print("FINISH")
game()

                
      



            


