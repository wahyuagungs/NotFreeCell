from enum import Enum
from core.color import Color


class CardColor(Enum):
    """
    This enum class will define the colour of every card in the game. 
    Each property will have 2 values comprises of an integer  and Colour Class Instance.
    """
    RED = 0, Color.RED
    BLACK = 1, Color.BLACK

    def __str__(self):
        return self.name

    # This method returns the exact byte value of a colour from Colour class
    def get_color_code(self):
        return self.value[1].value


