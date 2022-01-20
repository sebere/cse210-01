
board = [
    "1","2","3",
    "4","5","6",
    "7","8","9"
]
champ = None
def main():
    global champ
    board_print()
    player_move()



def player_move():
    for i in range(5):
        player = "X"
        move(player)
        winner()
        if champ != "X" and i < 4 :

            for j in range(3):
                player = "O"
                move(player)
                winner()

                if winner == "O":
                    print("Congratulations")
                    print()
                    break
        elif champ == "X":
            print("Congratulations")
            print()
            break

def move(player):
    position = int(input("choose a square (1-9): "))
    position -= 1
    board[position] = player
    board_print()

def winner():
    global champ
    line()
    vertical()
    diagonal()
    
def line():
    global champ
    if board[0]== board[1]==board[2] !="1":
        champ = board[0]
    elif board[3] ==  board[4] == board[5] != "1":
        champ = board[3]
    elif board[6] ==  board[7] == board[8] != "1":
        champ = board[6]
def vertical():
    global champ
    if board[0] ==  board[3] == board[6] != "1":
        champ = board[0]
    elif board[1] ==  board[4] == board[7] != "1":
        champ = board[1]
    elif board[2] ==  board[5] == board[8] != "1":
        champ = board[2]
def diagonal():
    global champ
    if board[0] ==  board[4] == board[8] != "-":
        champ = board[0]
    elif board[2] ==  board[4] == board[6] != "-":
        champ = board[2]

def board_print():
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-----')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-----')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()



if __name__ == "__main__":
    main()


 






