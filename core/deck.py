from core.card import Card
from core.cardsuit import CardSuit
from random import shuffle
from core.stack import Stack


class Deck(Stack):
    """
    This class is a representative of a collection of cards, it can create as many cards with as many variations as user lie
     It will use Stack as a base class to re-use existing method without to re-write its methods
    """

    # This will create a collection of cards, depending on what are the parameters given
    def __init__(self, value_start=1, value_end=13, suits_number=4):
        """This constructor method will give 3 initial values for creating a deck object
            value_start (default = 1) is the minimum value of a card suit which only can be started from 1 (Ace)
            value_end (default = 13) is the maximum value of a card suit in the maximum domain of 13 as King
            suit_number (default = 4) is the number of suit that will be createdd, e.g. value of 1 will 
            create only a suit of card
        """
        assert not value_end > 13 or value_start < 1 or suits_number > 4, print("Options card are not allowed")
        self._min = value_start  # minimum value of a card
        self._max = value_end + 1  # maximum value of a card
        self._suit_number = suits_number  # counter for creating suit, starts from Hearts
        self._count = 0
        super().__init__()

        # This code will create cards and append them inside a list called self._card_list
        i = 0
        while i < self._suit_number:
            m = i % 4
            if m == 0:
                # create bunch of cards and extend to the list
                out = Deck.__create_cards(self._min, self._max, CardSuit.SPADES)
            elif m == 1:
                # create bunch of cards and extend to the list
                out = Deck.__create_cards(self._min, self._max, CardSuit.HEARTS)
            elif m == 2:
                # create bunch of cards and extend to the list
                out = Deck.__create_cards(self._min, self._max, CardSuit.CLUBS)
            elif m == 3:
                # create bunch of cards and extend to the list
                out = Deck.__create_cards(self._min, self._max, CardSuit.DIAMONDS)
            i += 1
            super().add_cards(out)

    # this method uses shuffle function from random library to shuffle all cards
    def shuffle_card(self):
        shuffle(super().get_cards())

    # removes and returns the top item on the stack
    def draw_card(self):
        return super().pop()

    # override str function to give nice looking print text
    def __str__(self):
        for c in super():
            return str(c)

    # this is factory pattern method for creating each card and return a collection of card in a suit
    @staticmethod
    def __create_cards(min_val, max_val, suit):
        result_list = []
        for i in range(min_val, max_val):
            card = Card(i, suit)
            result_list.append(card)
        return result_list
