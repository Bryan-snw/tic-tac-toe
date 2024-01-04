from logo import logoArt

is_on = True
chance = 0
player = "O"
winning_condition = [
    [
        [1, 1], [1, 2], [1, 3]
    ],
    [
        [2, 1], [2, 2], [2, 3]
    ],
    [
        [3, 1], [3, 2], [3, 3]
    ],
    [
        [1, 1], [2, 1], [3, 1]
    ],
    [
        [1, 2], [2, 2], [3, 2]
    ],
    [
        [3, 3], [2, 3], [3, 3]
    ],
    [
        [1, 1], [2, 2], [3, 3]
    ],
    [
        [1, 3], [2, 2], [3, 1]
    ]
]
game_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


def check_winning_condition():
    for con in winning_condition:
        temp = 0
        for x in con:
            temp_row = x[0]
            temp_column = x[1]
            if game_board[temp_row - 1][temp_column - 1] == player:
                temp += 1
        if temp == 3:
            return True
    return False


def render_game_board():
    print("")
    for rw in range(len(game_board)):
        print(f"({rw + 1})", end='')
        for val in game_board[rw]:
            print(f" {val} ", end="|")
        print('')
    print("")


print(logoArt)
print("Welcome To Tic Tac Toe Game")
print("This game need 2 players to play")

while is_on and chance <= 9:
    render_game_board()
    print(f'Symbol {player} turn | Where you want to put')

    try:
        row = int(input("Which row (1/2/3): "))
        column = int(input("Which Column (1/2/3): "))
    except ValueError:
        print('Invalid input!, input must be number\n')
        continue

    try:
        # if it's still empty
        if game_board[row - 1][column - 1] == " ":
            game_board[row - 1][column - 1] = player
        else:
            print("That slot is already exist, try another row or column\n")
    except IndexError:
        print('Invalid input!, try another row or column\n')
    finally:
        if check_winning_condition():
            render_game_board()
            print(f'{player} Is The Winner!🎉')
            is_on = False
        else:
            chance += 1
            player = "X" if player == "O" else "O"
