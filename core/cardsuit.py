from enum import Enum
from core.cardcolor import CardColor


class CardSuit(Enum):
    """
    This enum class will be used to determine for an card suit, it has color's property from CardColor class
    and will return a UTF-8 symbol notation for every overridden operation that has been carried on.
    These symbols will represent of every face suit available and expected works in s UNIX-based system.
    """
    CLUBS = 'C', CardColor.BLACK
    HEARTS = 'H', CardColor.RED
    SPADES = 'S', CardColor.BLACK
    DIAMONDS = 'D', CardColor.RED

    # This will override CardSuit into a symbol in UTF-8
    # It works mostly on UNIX-based system
    # I got this Idea from http://fc-solve.shlomifish.org/
    def __str__(self):
        if self.name == 'DIAMONDS':
            return '◇'
        elif self.name == 'HEARTS':
            return '♡'
        elif self.name == 'SPADES':
            return '♠'
        elif self.name == 'CLUBS':
            return '♣'
        else:
            return self.name

    # returns color name from cardcolor instance
    def get_color_name(self):
        return self.value[1].name

    # returns color value in integer from cardcolor instance
    def get_color_value(self):
        return self.value[1].value

    # returns this class object value
    def get_value(self):
        return self.value[0]
