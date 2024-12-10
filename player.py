
class Player():
    def __init__(self, nr):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,41, 42, 43, 44, 45, 46, 47, 48, 49, 50,51, 52, 53, 54, 55, 56, 57, 58, 59, 60,61, 62, 63, 64, 65, 66, 67, 68, 69, 70,71, 72, 73, 74, 75, 76, 77, 78, 79, 80,81, 82, 83, 84, 85, 86, 87, 88, 89, 90,91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
        self.nr = nr

    def is_pick_next_to_before(self, picks, pick):

        if len(picks) == 0:
            return True

        ile = 0
        picks.sort()
        for i in range (1, len(picks)):
            if picks[i] == picks[i-1] + 10:
                ile += 1
            else:
                break
        if ile >= len(picks) - 1:
            if pick == picks[len(picks)-1] + 10:
                return True

        ile = 0
        for i in range (1, len(picks)):
            if picks[i] == picks[i-1] +1:
                ile += 1
            else:
                break
        if ile >= len(picks) - 1:
            if pick == picks[len(picks)-1] + 1:
                return True
        return False

    def set_board(self):

        # Ustawianie 4-masztowca
        print(f"Graczu {self.nr}! Ustaw swojego 4 masztowca!")
        picks = []
        i = 1
        while i < 5:
            pick = int(input(f"Wybierz {i} miejsce: "))
            if pick < 1 or pick > 100:
                print("Twój wybór musi być w przedziale 1-100!. Wybierz jeszcze raz.")
            elif self.board[pick - 1] == "S":
                print("To pole jest już zajęte. Wybierz jeszcze raz.")
            elif not self.is_pick_next_to_before(picks, pick):
                print("Statek musisz stawiać w jednej lini. Wybierz jeszcze raz.")
            else:
                i += 1
                picks.append(pick)
                self.board[pick -1] = "S"

        self.print_board()

        print(f"Graczu {self.nr}! Ustaw swoje dwa 3 masztowce!")
        for j in range(2):
            picks = []
            i = 1
            while i < 4:
                pick = int(input(f"Wybierz {i} miejsce: "))
                if pick < 1 or pick > 100:
                    print("Twój wybór musi być w przedziale 1-100!. Wybierz jeszcze raz.")
                elif self.board[pick - 1] == "S":
                    print("To pole jest już zajęte. Wybierz jeszcze raz.")
                elif not self.is_pick_next_to_before(picks, pick):
                    print("Statek musisz stawiać w jednej lini. Wybierz jeszcze raz.")
                else:
                    self.board[pick - 1] = "S"
                    picks.append(pick)
                    i += 1


    def print_board(self):
        for i in range(10):
            row_as_text = ""
            for j in range(10):
                row_as_text += str(self.board[i*10 + j]) + " "
            print(row_as_text)
