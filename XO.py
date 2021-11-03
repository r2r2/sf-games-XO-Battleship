import random

def greet():
    print("***********************************")
    print("Welcome to amazing Tic-Tac-Toe game")
    print("You'll eager to play with AI-XO_bot")
    print("Choose from 0 to 2                 ")
    print("Type in format N1 N2               ")
    print("N1 for row & N2 for colon          ")
    print("First turn X. Have fun!            ")
    print("***********************************")


def show_field():
    print("\t0\t1\t2")
    for i, row in enumerate(field):
        row_inf = "\t".join(row)
        print(f"{i}\t{row_inf}")
        print()


def xo_bot():
    mov_bot = random.choice(moves)
    moves.remove(mov_bot)
    return mov_bot


def ask_user():
    while True:
        mov = tuple(map(int, input("Make your move (N1_N2): ").split()))
        if mov in moves:
            moves.remove(mov)
            return mov
        else:
            print("You should choose 0-2 in format (N1 whitespace N2)!!!")


def win_conditions():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Winner - X !!!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Winner - O !!!")
            return True
    return False


greet()
field = [["-"] * 3 for _ in "123"]
moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
i = 1
while moves:
    show_field()
    if win_conditions():
        break
    if not moves:
        print("It's a draw.")
    if i % 2 == 1:
        mov = ask_user()
        field[mov[0]][mov[1]] = "X"
    else:
        mov_bot = xo_bot()
        field[mov_bot[0]][mov_bot[1]] = "O"
    i += 1