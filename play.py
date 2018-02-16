import sys
from src import commands, game

game = game.Game()
game.start()

while True:
    game.new_turn()
    instruction = sys.stdin.readline().strip().lower()
    game.interpret(instruction)


