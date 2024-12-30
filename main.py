from player import Player
import os
import time
print(r"""  ____ _____ _________          ____     __    __  __  ____  _____   _____ _  _______ ______ 
 |  _ \_   _|__   __\ \        / /\ \   / /   |  \/  |/ __ \|  __ \ / ____| |/ /_   _|  ____|
 | |_) || |    | |   \ \  /\  / /  \ \_/ /    | \  / | |  | | |__) | (___ | ' /  | | | |__   
 |  _ < | |    | |    \ \/  \/ /    \   /     | |\/| | |  | |  _  / \___ \|  <   | | |  __|  
 | |_) || |_   | |     \  /\  /      | |      | |  | | |__| | | \ \ ____) | . \ _| |_| |____ 
 |____/_____|  |_|      \/  \/       |_|      |_|  |_|\____/|_|  \_\_____/|_|\_\_____|______|
                                                                                             
                                                                                             """)

time.sleep(2)

print("""Zasady gry:
- 2 graczy,
- Flota 10 statków: 1 x 4 masztowiec, 2 x 3 masztowce, 3 x 2 masztowce, 4 x 1 masztowce,
- Statki mogą dotykać się brzegami,
- Gracze na początek ustawiają swoje statki, następnie przechodzimy do oddawania strzalów w przeciwnika (turowo),
- Jeżeli gracz 'trafi' statek przeciwnika, to w danej turze ma kolejny strzal (dopoki nie chybi)
- Gra kończy się, gdy jeden z graczy zestrzeli wszystkie statki przeciwnika.

__________________________________________________________________________________________________________________
""")

time.sleep(3)

print("""Legenda:

S - Miejsce Twoich statków
X - Miejsce Twojego strzału (pudło)
* - Miejsce Twojego strzału (trafiony cel)
0 - Miejsce strzału celnego przeciwnika
__________________________________________________________________________________________________________________""")


time.sleep(3)
input("Aby przejść dalej, kliknij ENTER.")
os.system('cls')

player1 = Player(1)
os.system('cls')
player2 = Player(2)
os.system('cls')



player1.set_board()
os.system('cls')


player2.set_board()
os.system('cls')


player1.set_enemy_board(player2.board)
player2.set_enemy_board(player1.board)

player1.set_enemy_ships(player2.ships)
player2.set_enemy_ships(player1.ships)



while True:
    os.system('cls')
    player1.shoot_or_show_board()
    # player1.shoot()
    os.system('cls')
    player2.shoot_or_show_board()
    # player2.shoot()