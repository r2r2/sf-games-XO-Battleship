class Field:

    def __init__(self):
        self.field = [["-"] * 3 for _ in "123"]

    def __str__(self):
        res = ""
        res += "\t0\t1\t2\n"
        for i, row in enumerate(self.field):
            row_inf = "\t".join(row)
            res += f"{i}\t{row_inf}\n"
        return res

    def in_field(self, x, y):
        return 0 <= x <= 2 and 0 <= y <= 2

    def get_char(self, x, y):
        if self.in_field(x, y):
            return self.field[x][y]
        else:
            raise ValueError("Out of range field")

    def set_char(self, x, y, char):
        if self.get_char(x, y) == "-":
            self.field[x][y] = char
        else:
            raise ValueError("Field is occupaid")

    def get_winner(self):
        win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                    ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
        for cord in win_cord:
            symbols = []
            for c in cord:
                symbols.append(self.field[c[0]][c[1]])
            if symbols == ["X", "X", "X"]:
                return "X"
            if symbols == ["O", "O", "O"]:
                return "O"
        return None


class ConsoleInterface:

    def __init__(self):
        self.greet()

    def greet(self):
        print("***********************************")
        print("Welcome to amazing Tic-Tac-Toe game")
        print("You'll eager to play with AI-XO_bot")
        print("Choose from 0 to 2                 ")
        print("Type in format N1 N2               ")
        print("N1 for row & N2 for colon          ")
        print("First turn X. Have fun!            ")
        print("***********************************")

    def show_field(self, field):
        print(field)

    def ask(self):
        while True:
            cords = input("Make your move (N1_N2): ").split()

            if len(cords) != 2:
                print(" Enter 2 coordinates")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Enter number! ")
                continue

            x, y = int(x), int(y)

            return x, y

    def current(self, char):
        print(f"Turn '{char}'!")

    def show_win(self, char):
        print(f"Winner is: '{char}'!")

    def draw(self):
        print("It's a draw!")

    def show_err(self, err):
        print(f"Error: {err}")


class App:

    def __init__(self):
        self.field = Field()
        self.cl = ConsoleInterface()

    def try_ask(self, char):
        while True:
            try:
                x, y = self.cl.ask()
                self.field.set_char(x, y, char)
            except ValueError as e:
                self.cl.show_err(e)
            else:
                break

    def loop(self):
        count = 0
        while True:
            if count % 2 == 0:
                char = "X"

            else:
                char = "O"

            self.cl.show_field(self.field)
            self.cl.current(char)

            self.try_ask(char)

            count += 1

            winner = self.field.get_winner()
            if winner:
                self.cl.show_field(self.field)
                self.cl.show_win(winner)
                break

            if count == 9:
                self.cl.draw()
                break


app = App()
app.loop()


























