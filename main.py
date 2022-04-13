from copy import deepcopy, copy

import player
import window

import game

if __name__ == '__main__':
    game = game.Game()
    game.make_a_move(1)
    game.make_a_move(2)
    game.make_a_move(1)
    game.make_a_move(2)
    game.make_a_move(1)
    game.make_a_move(2)
    game.make_a_move(1)
    game.make_a_move(2)
    window = window.Window()

    window.render(game.get_board())


