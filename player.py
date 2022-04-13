from enum import Enum


RED_PLAYER_COLOR = "#f00"
YELLOW_PLAYER_COLOR = "#ff0"

RED_PLAYER_LABEL = "Red"
YELLOW_PLAYER_LABEL = "Yellow"





class Player(Enum):

    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, label, text, color):
        self.label = label
        self.text = text
        self.color = color

    YELLOW = (1, YELLOW_PLAYER_LABEL, YELLOW_PLAYER_COLOR)
    RED = (2, RED_PLAYER_LABEL, RED_PLAYER_COLOR)

    def getLabel(self):
        return self.label

    def getText(self):
        return self.text

    def getColor(self):
        return self.color

    def get_next_player(self):
        return Player.YELLOW if self == Player.RED else Player.RED
