from core.color import Color


class Cell:
    """
    This class is the free cell class which can contain any card from any subset, however only a card can be placed 
     at a time. Without the possibility to override or stack the card on top of it.
     This cell will use the same convention standard name from stack, however it does not have behaviour list.
    """
    def __init__(self, location):
        self._card = None  # after initialized it will be None or empty
        self._location = location  # this will marked location of a cell

    # return False if empty and True if any card object exist
    def is_empty(self):
        return True if self._card is None else False

    # add card to the cell object
    def add_card(self, card):
        assert self.is_empty(), "Cannot place a card because it's occupied"
        self._card = card
        self._card.set_location(self._location)

    # returns a card if it is not empty
    def peek(self):
        return self._card if not self.is_empty() else None

    # remove card object from the object
    def pop(self):
        self._card.set_location(None)
        self._card = None

    # print card in using symbol and give different colors
    def __str__(self):
        return str(self._card) if not self.is_empty() else Color.BLUE.value + "-:-" + Color.BLUE.value

    # returns the location of cell object
    def get_location(self):
        return self._location
