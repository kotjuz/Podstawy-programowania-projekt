# Zasady: 10x10 plansza, 1x4 masztowiec, 2x3 masztowiec, 3x2 masztowiec, 4x1 masztowiec
from player import Player
import os
player1 = Player(1)
player2 = Player(2)
player1.print_board(player1.board)
player1.set_board()
os.system('cls')

player2.print_board(player2.board)
player2.set_board()
os.system('cls')

player1.set_enemy_board(player2.board)
player2.set_enemy_board(player1.board)

while True:
    player1.shoot()
    player2.shoot()