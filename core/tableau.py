from core.stack import Stack


class Tableau(Stack):
    """
    This class has the purpose to contain all the cards given when the first time game is being played.
    It uses Stack as its base class, and only contains 1 logic in
    """
    def __init__(self, location):
        self._location = location  # this will marked a location for each tableau object
        super().__init__()  # calling base class init method

    # check if a card has valid entry according rules
    def is_valid_card(self, card):
        if not super().is_empty():  # if there is no card in tableau stack, any card can be placed
            if super().peek().get_cardsuit().get_color_value() != card.get_cardsuit().get_color_value() \
                    and super().peek().get_number() == card.get_number() + 1:  # comparing card color and number
                return True
            else:
                return False
        else:
            return True

    # this method override base class to add validation
    def add_card(self, card, new_game=False):
        if not new_game:  # after being initialized, card will be distributed, this logic will prevent validation being invoked
            assert self.is_valid_card(card), "Cannot Add Card, You have either invalid suit or number"
        if self.is_valid_card(card) and not new_game:
            card.set_location(self._location)
            super().push(card)
        if new_game:
            card.set_location(self._location)
            super().push(card)

    # returns tableau location within the set
    def get_location(self):
        return self._location

    # set location of tableau object
    def set_location(self, location):
        self._location = location

    # this method is to prevent base class being invoked
    def add_cards(self, cards):
        raise NotImplementedError("Cannot take card from foundation")
