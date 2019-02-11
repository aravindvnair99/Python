def print_board(board):
    print("o-----o")
    
    for row in board:
        #removes quotation marks & replaces commas w/ lines
        for c in (("'", ''), (", ", "|")):
            row=str(row).replace(*c)
        print(row)
        
    print("o-----o")


#note: input() is used instead of int(input()) to handle errors when input is NaN
def choose_cell(board, turn):
    cell = input("Player " + str(turn) + ", what cell will you make a move on? (1-9): ")
    
    #while input cell is invalid, keep asking for input
    while check_if_valid_cell(cell) == False:
        cell = input("Input invalid. Please input a cell to make a move on. (1-9): ")

    cell = int(cell)
    row = get_row(cell)
    col = get_col(cell)

    #sets cell to X or O depending on turn (P1 = 'X', P2 = 'O')    
    if turn == 1:
        board[row][col] = "X"
    else:
        board[row][col] = "O"


def check_if_valid_cell(cell):
    #checks and runs if input is a number
    if cell.isdigit():
        cell = int(cell)

        #checks if input cell is empty
        if cell >= 1 and cell <= 9 and check_if_empty_cell(get_row(cell), get_col(cell)) == True:
            return True
        else:
            return False

    #runs if input is not a number
    else:
        return False

        
def get_row(cell):
    #returns row index of cell (0-2)
    if cell%3 == 0:
        return int(cell/3)-1
    else:
        return int(cell/3)


def get_col(cell):
    #returns column index of cell (0-2)
    if cell%3 == 0: 
         return 2
    else:
         return (cell%3)-1


def check_if_empty_cell(row, col):
    #if cell holds a number, cell is empty
    if str(board[row][col]).isdigit():
        return True
    else:
        return False

    
def win():
    if (#Horizontal combinations
        board[0][0]==board[0][1]==board[0][2] or
        board[1][0]==board[1][1]==board[1][2] or
        board[2][0]==board[2][1]==board[2][2] or
        #Vertical combinations
        board[0][0]==board[1][0]==board[2][0] or
        board[0][1]==board[1][1]==board[2][1] or
        board[0][2]==board[1][2]==board[2][2] or
        #Diagonal combinations
        board[0][0]==board[1][1]==board[2][2] or
        board[0][2]==board[1][1]==board[2][0]):
        
        print_board(board)
        print("Player", switch_turn(turn), "has won the game! Congratulations!")
        return True
    else:
        return False


def tie():
    is_tie = True
    
    #if any number exists in board, board is not tied
    for a in range(1, 10):
        for row in board:
            if a in row:
                is_tie = False
                return False

    #runs if board is tied
    if is_tie:
        print_board(board)
        print("The game has ended in a tie!")
        return True


def switch_turn(turn):
    #switches turn from 1 to 2 and vice versa
    if turn == 1:
        turn+=1
    else:
        turn-=1
        
    return turn


def ask_replay():
    response = input("Game Over! Play again? (Y/N): ")

    #while response is invalid, keep asking for input
    while(response != "Y" and response != "N"):
        print("Please input Y to replay and N to stop playing.")
        response=input("Play again? (Y/N) : ")

    if response == "Y":
        return True
    else:
        return False

    
#actual game
replay = True

while replay == True:
    board = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    turn = 1
    
    while (win() or tie()) == False:
        print_board(board)
        choose_cell(board, turn)
        turn = switch_turn(turn)
            
    replay = ask_replay()
