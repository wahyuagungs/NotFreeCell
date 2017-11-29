from core.stack import Stack
from core.color import Color


class Foundation(Stack):
    """
    This class is sometimes called as winner deck, because it will hold stack of cards that will be moved from either
    Tableau or Cells. All cards must be placed according to its suit and number sequentially. 
    The number of foundation object will depend on the number of suits that will be created in the beginning, with the 
    exception of if the number of suits is less than 4, the number of foundation will only still be 4.
    """
    def __init__(self, location):
        self._location = location
        self._type = None
        super().__init__()

    # only give the top card if exists, assuming that all cards will be in order
    def __str__(self):
        return str(super().peek()) if not self.is_empty() else Color.GREEN.value + '-:-' + Color.GREEN.value

    # this method override base class to add validation
    def add_card(self, card):
        if super().is_empty():
            if card.get_number() == 1: # first card must be an ace of any suit
                card.set_location(self._location) # set every card in the same object location of foundation
                super().add_card(card)
                self._type = card.get_cardsuit() # it will set the object
            else:
                raise Exception("The first card must be an ACE of any suit")
        else:
            # comparing the type and the number which will be equivalent of new card number = top list - 1
            if card.get_cardsuit() is self._type \
                    and card.get_number() == super().peek().get_number() + 1:
                card.set_location(self._location)
                super().add_card(card)
            else:
                raise Exception("Cannot add card for different type or unmatched number")

    # returns location of foundation
    def get_location(self):
        return self._location

    # set location of foundation
    def set_location(self, location):
        self._location = location

    # this method is to prevent base class being invoked
    def add_cards(self, cards):
        raise NotImplementedError("Cannot take card from foundation")
