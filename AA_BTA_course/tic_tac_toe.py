board=[" " for i in range(9)]

def print_board():
    print(board)

    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)

def player_game(icon):

    if icon == "#":
        number=1
    elif  icon == "X":
        number=2
    print("  player {} your turn !".format(number))

    choice =int(input("Enter you digit between 1 to 9  : ").strip())
    if board[choice-1] == " ":
        board[choice-1]=icon
    else:
        print()
        print("OOPS!! it is already marked ..")
    #print(board )

def is_victory(icon):
    if ( board[0]==icon and board[1]==icon and board[2] or \
        board[3]==icon and board[4]==icon and board[5]  or  \
        board[6]==icon and board[7]==icon and board[8]  or \
        board[0]==icon and board[3]==icon and board[6] or \
        board[1]==icon and board[4]==icon and board[7]  or \
        board[2]==icon and board[5]==icon and board[8] or \
        board[0]==icon and board[4]==icon and board[8] or \
        board[2]==icon and board[4]==icon and board[6]) :
            return True
    else :
                return False

def is_draw():
    if " " not in board :
        return True
    else:
        return False

while True:
    print_board()
    player_game("#")
    print_board()
    if is_victory("#"):
        print_board()
        print(" Congratulations player # won" )
        break
    if is_draw():
        print("The gaame is draw")

    player_game("X")
    if is_victory("X"):
        print_board()
        print(" Congratulations player X won" )
        break
