import random,sys,time
n=[" " for i in range(9)]
board=[" " for j in range(1,10)]
# print(board)
# print(n)
def print_board():
    row1="| {} | {} | {} |".format(board[0],board[1],board[2])
    row2="| {} | {} | {} |".format(board[3],board[4],board[5])
    row3="| {} | {} | {} |".format(board[6],board[7],board[8])
    print(row1)
    print(row2)
    print(row3)
# x=random.randint(1,9)
# print(x)
# print_board()
def player_move(icon):
    if icon=='X':
        num=1
    elif icon=="O":
        num=0
    if icon=='X':
        print("Player-1  turn----")
    elif icon=='O':
        print("Player-2 turn------")
    choice=int(input("Enter num between 1-9:"))
    if choice>0 and choice<=9:
        if board[choice-1]==" ":
            board[choice-1]=icon
        else:
            player_move(icon)
    # print(print_board())
def computer_move(icon):
    if icon=='X':
        num=1
    elif icon=="O":
        num=0
    print("computer turn----")
    choice=random.randint(1,9)    
    if board[choice-1]==" ":
        board[choice-1]=icon
    else:
        computer_move(icon)

def is_win(icon):
    if (board[0]==icon and board[1]==icon and board[2]==icon or\
        board[3]==icon and board[4]==icon and board[5]==icon or\
        board[6]==icon and board[7]==icon and board[8]==icon or\
        board[0]==icon and board[3]==icon and board[6]==icon or\
        board[1]==icon and board[4]==icon and board[7]==icon or\
        board[2]==icon and board[5]==icon and board[8]==icon or\
        board[0]==icon and board[4]==icon and board[8]==icon or\
        board[6]==icon and board[4]==icon and board[2]==icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False


while True:
    ch=int(input("Which mode you want to play: 1.Player vs Player  2.Computer vs PPlayer :"))
    if ch==2:
        while True:
            # Player turn------------------------
            print_board()
            player_move("X")
            # print_board()
            if is_win("X"):
                print_board()

                print("player X wins ...Congratulations .........")
                sys.exit()
            elif is_draw():
                print("It is Draw")

            # computer turn-------------------------
            print_board()
            computer_move("O")
            # print_board()
            if is_win("O"):

                print("player O wins ...Congratulations .........")
                sys.exit()
            elif is_draw():
                print("It is Draw")


    elif ch==1:
        while True:
            # Player turn------------------------
            print_board()
            player_move("X")
            # print_board()
            if is_win("X"):
                print_board()

                print("player X wins ...Congratulations .........")
                sys.exit()
            elif is_draw():
                print("It is Draw")
            # Player turn------------------------
            print_board()
            player_move("O")
            # print_board()
            if is_win("O"):
                print_board()

                print("player O wins ...Congratulations .........")
                sys.exit()
            elif is_draw():
                print("It is Draw")

           
    else:
        print("Enter again:")





