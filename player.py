import sys
import os
import time

class Player:
    def __init__(self, nr):
        self.board = list(range(1, 101))
        self.shoots_board = list(range(1, 101))
        self.enemy_board = []
        self.ships = []
        self.enemy_ships = []
        self.nr = nr
        self.name = self.set_name()




    def set_name(self):
        name = input(f"Graczu {self.nr}! Wybierz swoje imie: ")
        return name

    def set_enemy_board(self, enemy_board):
        self.enemy_board = enemy_board

    def set_enemy_ships(self, enemy_ships):
        self.enemy_ships = enemy_ships

    def print_remaining_enemy_ships(self):

        ship_types = [
            (4, 1),
            (3, 2),
            (2, 3),
            (1, 4),
        ]

        for ship in self.enemy_ships:
            for i in range(len(ship)):
                if ship[i] != "X" and self.shoots_board[ship[i] - 1] == "*":
                    ship[i] = "X"


        for ship_size, count in ship_types:
            for ship in self.enemy_ships:
                if len(ship) == ship_size:
                    if all(position == 'X' for position in ship):
                        print("X" * ship_size)
                    else:
                        print("■" * ship_size)




    def is_pick_next_to_before(self, picks, pick):
        if not picks:
            return True

        picks.sort()
        in_line_vertical = all(picks[i] == picks[i - 1] + 10 for i in range(1, len(picks)))
        in_line_horizontal = all(picks[i] == picks[i - 1] + 1 for i in range(1, len(picks)))

        if in_line_vertical and (pick == picks[-1] + 10 or pick == picks[0] - 10):
            return True
        if in_line_horizontal and (pick == picks[-1] + 1 or pick == picks[0] - 1):
            return True

        return False

    def check_for_space(self, how_many, pick):
        ile = 0

        for i in range(pick - 1 + 10, 100, 10):
            if self.board[i] != "S":
                ile += 1
                if ile >= how_many:
                    return True
            else:
                break

        for i in range(pick -1 - 10, -1, -10):
            if self.board[i] != "S":
                ile += 1
                if ile >= how_many:
                    return True
            else:
                break

        ile = 0
        tmp_pick = pick
        last_digit = pick % 10
        if last_digit == 0:
            last_digit = 10
        for i in range(last_digit, 10):
            if self.board[tmp_pick - 1] != "S":
                ile += 1
                tmp_pick += 1
                if ile >= how_many:
                    return True
            else:
                break

        for i in range(last_digit - 1, 0, -1):
            if self.board[tmp_pick - 1] != "S":
                ile += 1
                tmp_pick -= 1
                if ile >= how_many:
                    return True
            else:
                break

        return False

    def set_board(self):
        def place_ship(size, count):
            for i in range(count):
                self.print_board(self.board)
                picks = []
                print(f"Ustaw swój {size}-masztowiec!")
                while len(picks) < size:
                    pick = int(input(f"Wybierz {len(picks) + 1} miejsce: "))
                    if len(picks) < 1 and not self.check_for_space(size, pick):
                        print("Nie możesz tutaj postawić statku, ponieważ nie zmieścisz go calego. Spróbuj ponownie.")
                    elif pick < 1 or pick > 100:
                        print("Twój wybór musi być w przedziale 1-100. Spróbuj ponownie.")
                    elif self.board[pick - 1] == "S":
                        print("To pole jest już zajęte. Spróbuj ponownie.")
                    elif not self.is_pick_next_to_before(picks, pick):
                        print("Statek musi być w jednej linii. Spróbuj ponownie.")
                    else:
                        picks.append(pick)
                        self.board[pick - 1] = "S"
                self.ships.append(picks)
                os.system("cls")

        print(f"Graczu {self.name}! Ustaw swoje statki.")
        time.sleep(1.5)
        place_ship(4, 1)
        place_ship(3, 2)
        place_ship(2, 3)
        place_ship(1, 4)


    def print_board(self, board):
        cell_width = 3
        horizontal_border = "+" + "-" * (10 * (cell_width + 1) + 1) + "+"

        print(horizontal_border)
        for i in range(0, len(board), 10):
            row = board[i:i + 10]
            row_content = "| " + " ".join(f"{cell:>{cell_width}}" for cell in row) + " |"
            print(row_content)
        print(horizontal_border)




    def shoot_or_show_board(self):
        print(f"Graczu {self.name}! Twoja kolej.")
        print("""+-------------------------------------+
|                                     |
|     1. Oddaj strzał                 |
|     2. Zobacz swoją planszę         |
|                                     |
+-------------------------------------+
""")
        chose = input(": ")
        if chose != "1" and chose != "2":
            print("Masz do wyboru tylko '1' lub '2', nic wiecej.")
            time.sleep(1.5)
            os.system("cls")
            self.shoot_or_show_board()
        elif chose == "1":
            os.system("cls")
            self.shoot()
        elif chose == "2":
            os.system("cls")
            self.print_board(self.board)
            input("Aby wyjsc, nacisnij ENTER.")
            os.system("cls")
            self.shoot_or_show_board()


    def shoot(self):
        self.print_remaining_enemy_ships()
        self.print_board(self.shoots_board)
        print(f"Graczu {self.name}! Twoja kolej na strzal")
        pick = int(input("Twój strzal: "))

        while self.enemy_board[pick - 1] == "S":
            os.system("cls")
            self.shoots_board[pick - 1] = "*"
            self.enemy_board[pick - 1] = 0
            self.print_remaining_enemy_ships()
            self.print_board(self.shoots_board)
            print("Brawo! Trafiles!")
            if self.check_for_win():
                os.system("cls")
                print(f"Koniec gry! Gracz {self.name} wygrywa!")
                time.sleep(2)
                sys.exit()
            pick = int(input("Twój kolejny strzal: "))

        os.system("cls")
        self.shoots_board[pick - 1] = "X"
        self.print_board(self.shoots_board)
        print("Pudlo! Kolej przeciwnika.")
        time.sleep(1)


    def check_for_win(self):
        for i in range(100):
            if self.enemy_board[i] == "S":
                return False
        return True

