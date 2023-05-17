# import sys
def tic_tac_toe():
    board = [' ' for x in range(10)]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw():
        print('\t\t\t|-----------|')
        print('\t\t\t|   |   |   |')
        print('\t\t\t| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' | ')
        print('\t\t\t|   |   |   |')
        print('\t\t\t|-----------|')
        print('\t\t\t|   |   |   |')
        print('\t\t\t|  ' + board[3] + '| ' + board[4] + ' | ' + board[5] + ' | ')
        print('\t\t\t|   |   |   |')
        print('\t\t\t|-----------|')
        print('\t\t\t|   |   |   |')
        print('\t\t\t|  ' + board[6] + '| ' + board[7] + ' | ' + board[8] + ' | ')
        print('\t\t\t|   |   |   |')
        print('\t\t\t|-----------|')

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:

             board[n] = "X"
           
    def p2():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a  = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                   print("\nThat's not a number. Try again")
                   continue

    Player_one = input("Player 1 provide your name:")
    Player_two = input("Plater 2 provide your name:")
    
    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print(f"{Player_one} Wins!\n")
                print("Congratulations!\n")
                return True

            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print(f"{Player_two} Wins!\n")
                print("Congratulations!\n")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        if end == True:
            break
        # name = input('Player 1, provide your name:')
        
        
        # print("Player one choose where to place a cross")
        print(f"{Player_one} choose where to place a cross")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        # print("Player 2 choose where to place a nought")
        print(f"{Player_two} choose where to place a nought")
        p2()
        print()

    again2 = input("Play again (y/n)\n")
    if  "y" in again2 or "yes" in again2:
        print("<--*--@@@@@ TIc_Tac_Toe @@@@@--*-->")
        print()
        tic_tac_toe()
    elif "n" in again2 or "no" in again2:
        print("Hope you had fun while playing the tic tac toe!!!! \n")
        
        return None

    else:
        print("Invalid response!!!")
tic_tac_toe()