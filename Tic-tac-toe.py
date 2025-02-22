from random import randrange

print("""Гра хрестики-нулики
Правила:
1. Починає комп\'ютер
2. Гравець грає за нулики, комп\'ютер за хрестики""")

def display_board(board):
    print("+-------" *3,"+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|  ", str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")
    


def human_move(board):
    good = False
    while not good:
        your_move=int(input("Ваш хід: "))
        if your_move > 9 or your_move < 1:
            print("Введіть інше число!")
            continue
        your_move=int(your_move) - 1
        row = your_move // 3
        col = your_move % 3
        sign = board[row][col]
        good = sign not in ["O", "X"]
        if not good:
            print("Це поле вже зайнято, виберіть інше")
            continue
    board[row][col] = "O"
    


def make_list_of_free_fields(board):
    free_space=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["O", "X"]:
                free_space.append((row, col))
    return free_space
    


def winner_for(board, sgn):
    winner = False
    if sgn == "X":
        who = "me"
    elif sgn == "O":
        who = "you"
    else: who = None
    cros1=cros2=True
    for check in range(3):
        if board[check][0] == sgn and board[check][1] == sgn and board[check][2] == sgn:
            return who
        if board[0][check] == sgn and board[1][check] == sgn and board[2][check] == sgn:
            return who
        if board[check][check] != sgn:
            cros1 = False
        if board[2 - check][2 - check] != sgn:
            cros2 = False
    if cros1 or cros2:
        return who
    return None
        
    


def comp_move(board):

    free_field = make_list_of_free_fields(board)
    check = len(free_field)
    if check > 0:
        turn = randrange(check)
        row, col = free_field[turn]
        board[row][col] = "X"


board = [[i + 3 * j + 1 for i in range(3)] for j in range(3)]

board[1][1] = "X"
free = make_list_of_free_fields(board)
human_turn = True

while len(free):
    display_board(board)
    if human_turn:
        human_move(board)
        winner = winner_for(board, "O")
    else:
        comp_move(board)
        winner = winner_for(board, "X")
    if winner != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if winner == "you":
    print("Ви перемогли!")
elif winner == "me":
    print("Ви програли!")
else: print("Нічия!")

