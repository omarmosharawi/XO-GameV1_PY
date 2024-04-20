def printBoardView():
    print('1' + ' | ' + '2' + ' | ' + '3')
    print('--+---+--')
    print('4' + ' | ' + '5' + ' | ' + '6')
    print('--+---+--')
    print('7' + ' | ' + '8' + ' | ' + '9')
    print()

def printBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])

def game():
    print("\n### Welcome to XO Game! @omarmosharawi ###\n")
    print("* Instructions: ")
    print("- Each player takes turns placing their mark ('X' or 'O') on the board.")
    print("- The goal is to get three of your marks in a row (horizontally, vertically, or diagonally).")
    print("- If all positions are filled and no one has three in a row, it's a tie.")
    print("- Enter the number (1-9) corresponding to the position you want to mark.")
    print("- Avoid entering invalid positions or already filled positions.")
    print('- This is an numbers positions:')
    printBoardView()
    print("*** Let's begin! ***")

    theBoard = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
    }
    turn = 'X'
    count = 0

    while True:
        printBoard(theBoard)
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()

        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the top
                printBoard(theBoard)
                print("\n\tGame Over.")
                print("***** " + turn + " won! *****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\n\tGame Over.")
                print("***** " + turn + " won! *****")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\n\tGame Over.")
                print("***** " + turn + " won! *****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\n\tGame Over.")
                print("***** " + turn + " won! *****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\n\tGame Over.")
                print("***** " + turn + " won! *****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\n\tGame Over.")
                print("***** " + turn + " won! *****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\n\tGame Over.")
                print("***** " + turn + " won! *****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\n\tGame Over.")
                print("***** " + turn + " won! *****")
                break

        if count == 9:
            print("\nGame Over.")
            print("It's a Tie!!!")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    while True:
        play_again = input("\nDo you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            game()
            break
        elif play_again.lower() == 'n':
            print("Thanks for playing! Exiting...")
            print('Game Powered By Omar Mohamed Sharawi')
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")



if __name__ == "__main__":
    game()