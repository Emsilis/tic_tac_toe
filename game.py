def welcome():
    """Prints out the welcome message for the game"""
    print("Welcome to Tic Tac Toe\n")
    print("The game board is numbered from 1 to 9 starting from the bottom left corner")
    numbered_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    display_board(numbered_board)


def display_board(board):
    """
    Prints out the game board
    :param board: required; list(9) of integers or strings
    :return:
    """
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("\n")


def want_to_play():
    """
    Asks a player if they want to play until it gets a valid input
    Valid inputs: Yes, Y, No, N
    :return string
    """
    play = None
    while play is None:
        player_choice = input("Do you want to play? Yes (Y) or No (N)\n")
        play = want_to_play_input(player_choice)
    return play


def want_to_play_input(player_choice):
    """
    Based on player_choice parameter sends back
    if the player wants to play more (True)
    or not (False)
    or it is not a valid input (None)
    :param player_choice: required; string
    :return bool | None
    """
    if player_choice == "Yes" or player_choice == "Y":
        return True
    if player_choice == "No" or player_choice == "N":
        return False
    else:
        return None


def which_sign():
    """
    Asks a player which sign they want to play with until it gets a valid input
    Valid inputs: X, x, O, o
    :return string
    """
    sign = None
    while sign is None:
        sign_choice = input("Which sign would you like to be? X or O\n")
        sign = which_sign_input(sign_choice)
    return sign


def which_sign_input(sign_choice):
    """
    Based on sign_choice parameter sends back
    the sign the player wants to play with (X) or (O)
    or it is not a valid input (None)
    :param sign_choice: required; string
    :return string | None
    """
    if sign_choice == "X" or sign_choice == "x":
        return "X"
    if sign_choice == "O" or sign_choice == "o":
        return "O"
    else:
        return None


def other_player(sign1):
    """
    Based on player1's sign choice it sets player2's to the remaining sign
    :param sign1: required; string
    :return string
    """
    if sign1 == "X":
        return "O"
    else:
        return "X"


def put_sign_where():
    """
    Asks the player on where they want to place their sign (1-9)
    :return int
    """
    valid_number = False
    while not valid_number:
        place = input("Place your sign (1-9)\n")
        try:
            place = int(place)
            if 1 <= place <= 9:
                return place
        except:
            continue


def check_board(place, board):
    """
    Checks if the place where the player wanted to put their sign is empty (" " str)
    :param place: required; int
    :param board: required; list of 9 str
    :return: bool
    """
    return board[place - 1] == " "


def update_board(turn, player1_sign, board, place):
    """
    Based on turn and the player_sign parameter updates the board in the indicated place
    :param turn: required; int
    :param player1_sign: required; str
    :param board: required; list of 9
    :param place: required; int
    :return: list of 9
    """
    if turn % 2 == 1:
        board[place - 1] = player1_sign
        return board
    else:
        board[place - 1] = other_player(player1_sign)
        return board


def put_sign(turn, player1_sign, board):
    """
    Puts a new sign on the board
    :param turn: required; int
    :param player1_sign: required; str
    :param board: required; list of 9 str
    :return: list of 9 str
    """
    valid = False
    place = None
    while not valid:
        place = put_sign_where()
        valid = check_board(place, board)
    board = update_board(turn, player1_sign, board, place)
    return board


def check_for_game_over(board):
    """
    Checks the game board if there's a winner or stalemate
    :param board: required; list of 9 str
    :return: bool, str|None
    """
    if board[6] != " " and board[6] == board[7] == board[8]:
        return True, board[6]
    if board[6] != " " and board[6] == board[4] == board[2]:
        return True, board[6]
    if board[6] != " " and board[6] == board[3] == board[0]:
        return True, board[6]
    if board[7] != " " and board[7] == board[4] == board[1]:
        return True, board[7]
    if board[8] != " " and board[8] == board[4] == board[0]:
        return True, board[8]
    if board[8] != " " and board[8] == board[5] == board[2]:
        return True, board[8]
    if board[3] != " " and board[3] == board[4] == board[5]:
        return True, board[3]
    if board[0] != " " and board[0] == board[1] == board[2]:
        return True, board[0]
    if " " not in board:
        return True, None
    else:
        return False, None


def game():
    """
    The main part of the game
    """
    # ASKS IF THE PLAYER WANTS TO PLAY
    play = want_to_play()
    if not play:
        exit()
    # ASSIGN SIGNS
    player1_sign = which_sign()
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    game_over = False
    winner = None
    turn = 1
    # PUT SIGNS ON THE BOARD & CHECK FOR WIN CONDITION
    while not game_over:
        board = put_sign(turn, player1_sign, board)
        display_board(board)
        turn += 1
        game_over, winner = check_for_game_over(board)
    # WRITE OUT THE WINNER OR IF IT'S STALEMATE
    if winner is None:
        print("It's a stalemate")
    else:
        print(f"{winner} wins!")


if __name__ == "__main__":
    welcome()
    while True:
        game()
