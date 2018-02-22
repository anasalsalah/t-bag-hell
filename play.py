import sys
from src import game

game = game.Game(True, 0.00)

while True:
    game.new_turn()
    instruction = sys.stdin.readline().strip().lower()
    game.interpret(instruction)


