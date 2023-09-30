def draw_board(board):
    print("    A   B   C   D   E   F   G   H")
    print("  ---------------------------------")
    for i in range(8):
        print(str(i+1) + " |", end='')
        for j in range(8):
            print(" " + board[i][j] + " |", end='')
        print()
        print("  ---------------------------------")




def getPlace(Board, wB):
    while True:
        inpt = input("Please enter where you want to place and what you want to place. Either rook or pawn in this format: 'rook a4':").lower().strip()
        if inpt == "done" and wB == 'b':
            return inpt
        elif inpt == "done" and wB == 'w':
            continue
        else:
            figure_choice, place = inpt.split()
            figure_choice = figure_choice.strip()
            y = int(ord(place[0]))-97
            x = int(place[1])-1
            if 0 <= x <= 7 and 0 <= y <= 7:
                if figure_choice == 'rook' or figure_choice == 'pawn':
                    if Board[x][y] == " ":
                        return figure_choice, x, y
                    else:
                        print("That place is already taken")
                else:
                    print("Invalid Piece")
            else:
                print("Invalid Placement")
                




def check_up(board, n, m):
    while n >= 0:
        if board[n][m] == 'X':
            m = chr(m+97)
            return m + str(n + 1)
        else:
            n -= 1
            continue


def check_down(board, n, m):
    while n <= 7:
        if board[n][m] == 'X':
            m = chr(m+97)
            return m + str(n + 1)
        else:
            n += 1
            continue


def check_right(board, n, m):
    while m <= 7:
        if board[n][m] == 'X':
            m = chr(m+97)
            return m + str(n + 1)
        else:
            m += 1
            continue


def check_left(board, n, m):
    while m >= 0:
        if board[n][m] == 'X':
            m = chr(m+97)
            return m + str(n + 1)
        else:
            m -= 1
            continue


def checkrook(board, n , m):
    up = check_up(board, n, m) 
    down = check_down(board, n, m)
    left = check_left(board, n, m)
    right = check_right(board, n, m)
    if up:
        print(up, end=' ')
    if down:
        print(down, end=' ')
    if left:
        print(left, end=' ')
    if right:
        print(right)




def check_lDown(board, n, m):
    if board[n+1][m-1] == 'X':
        print(chr(m+96) + str(n + 2), end=' ')


def check_rDown(board, n, m):
    if board[n+1][m+1] == 'X':
        print(chr(m+98) + str(n + 2), end='')

        
def checkpawn(board, n, m):
    if n != 7:
        if m == 0:
            check_rDown(board, n, m)
        elif m == 7:
            check_lDown(board, n, m)
        else:
            check_lDown(board, n, m)
            check_rDown(board, n, m)
        print()
        
        


def main():
    board = [[" " for i in range(8)] for j in range(8)]
    draw_board(board)

    #White player
    choice_white, n, m = getPlace(board, 'w')
    board[n][m] = 'O'
    draw_board(board)

    #Black player
    black_count = 0
    while black_count < 16:
        black = getPlace(board, 'b')
        if isinstance(black, str):
            if black == 'done' and black_count > 0:
                break
            else:
                print("You have to atleast place one piece")
                continue
        else:
            Choice, x, y = black
            board[x][y] = 'X'
            draw_board(board)
            black_count = black_count + 1

    if choice_white == 'rook':
        checkrook(board, n, m)
    else:
        checkpawn(board, n, m)


main()