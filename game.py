import constant
from copy import deepcopy, copy

import player


class Game:
    def __init__(self):
        self.__board = deepcopy(constant.INIT_BOARD)
        self.__move_cnt = 0
        self.__move = constant.STARTING_PLAYER
        self.__winner = None

    def get_cell(self, x, y):
        return self.__board[x][y]

    def get_board(self):
        return deepcopy(self.__board)

    def show_available_moves(self):
        available = []
        for i in range(0, constant.BOARD_WIDTH):
            if self.__board[0][i] == constant.EMPTY_SPACE_LABEL:
                available[i] = 1  # You can make a move here
            else:
                available[i] = 0
        return available

    def announce_winner(self):
        if self.__winner is None:
            print("Game has no winner (yet!)")
        else:
            print("The winner is ", self.__winner)

    def make_a_move(self, col_num):
        if self.__winner is not None:
            return

        row = constant.BOARD_HEIGHT - 1

        player_that_moved: player.Player = None

        while row >= 0:
            if self.__board[row][col_num] == constant.EMPTY_SPACE_LABEL:
                self.__board[row][col_num] = self.__move.getLabel()
                player_that_moved = self.__move
                self.__move = self.__move.get_next_player()

                break
            row -= 1
        self.__move_cnt += 1

        if player_that_moved is None:
            # TODO: Raise an exception here
            return

        # Searching for victory

        # upwards
        r = row
        c = col_num
        seq = 1
        while r - 1 >= 0:
            r -= 1
            if self.__board[r][c] == player_that_moved.getLabel():
                seq += 1
                print("In streak ", seq)
                if seq == 4:
                    self.__winner = player_that_moved
                    self.announce_winner()
                    return

        # downwards
        r = row
        c = col_num
        seq = 1

        while r + 1 < constant.BOARD_HEIGHT:
            r += 1
            if self.__board[r][c] == player_that_moved.getLabel():
                seq += 1
                print("In streak ", seq)
                if seq == 4:
                    self.__winner = player_that_moved
                    self.announce_winner()
                    return
