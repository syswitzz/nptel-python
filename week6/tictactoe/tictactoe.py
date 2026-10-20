import os
import numpy


choices = ["O", "X", "-"]
standard_board = numpy.array([["-","-", "-"],["-","-","-"],["-","-","-"]])

def display_board(board):
    print("")
    print(numpy.matrix(board))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def rows():
    return [i for i in range(1, len(standard_board)+1)]

def check_row(board):
    for row in board:
        if row[0]==row[1]==row[2] and row[0] != choices[2]:
            return True
    return False

def check_col(board):
    for i in range(len(rows())):
        if (board[0][i] ==  board [1][i] == board[2][i]) and board[0][i] != choices[2]:
            return True
    return False

def check_diagonal(board):
    if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != choices[2]:
        return True
    else:
        False

def iswon(board):
    return check_col(board) or check_diagonal(board) or check_row(board)


def play():
    p1 = input("Enter player 1 name: ")
    p2 = input("Enter player 2 name: ")

    turn = 0

    while True:
        board = standard_board

        if turn % 2 == 0:
            # player 1 turn
            print(f"\n------ {p1}'s Turn ------")

            row = int(input(f"Enter Row {rows()}: "))
            col = int(input(f"Enter Column {rows()}: "))


            if row not in rows() or col not in rows() or board[row-1][col-1] != "-":
                print("Invalid choice!")
                continue

            board[row-1][col-1] = choices[0]
                

            display_board(board)

            if iswon(board):
                print(f"\nYay {p1} Won!")
                break
            
        else:
            # player 2 turn
            print(f"\n------ {p2}'s Turn ------")

            row = int(input(f"Enter Row {rows()}: "))
            col = int(input(f"Enter Column {rows()}: "))

            if row not in rows() or col not in rows() or board[row-1][col-1] != "-":
                print("Invalid choice!")
                continue

            board[row-1][col-1] = choices[1]

            display_board(board)

            if iswon(board):
                print(f"\nYay {p2} Won!")
                break

        turn += 1
        

clear()
play()