
class Card:
    ''' This is the Card Class
        Color will have two types : red and black, red will be using a 0 value and black will using 1 as a constant.
        The Color will be using Enum Type of color inside cardcolor.
        Inside a card, a number will be assigned for each card from 1 (Ace) to 13 (King).
        shape will have four types : diamonds, hearts, spades, and clubs using Enum of Card.
        There will be only 52-card types, ignoring the jokers.
    '''

    def __init__(self, number, suit, location=None):
        '''This is the constructor card method
            It will take number and suit as arguments to construct itself
            The card's color will be determined by the suit inside class cardsuit
        '''
        # This is a static method for validating number of card
        assert Card.__is_valid(number), "Invalid number of card"
        self._number = number
        self._suit = suit
        self._color = suit.get_color_name()
        self._location = location

    def __str__(self):
        ''' This override method
            will return the value of each card with its suit.
            For example,
            - Ace of Spade will be shown as A:S
            - Queen of Heart will   be shown as Q:H
            - 5 Club will be shown as 5:C
        '''
        if self._number == 1:
            temp = "A:" + str(self._suit)
        elif self._number == 11:
            temp = "J:" + str(self._suit)
        elif self._number == 12:
            temp = "Q:" + str(self._suit)
        elif self._number == 13:
            temp = "K:" + str(self._suit)
        else:
            temp = str(self._number) + ":" + str(self._suit)
        color_code = self._suit.get_color_value()[1].value
        return color_code + temp + color_code

    # returns color name as an accessor
    def get_color(self):
        return self._color

    # returns cardsuit object as an accessor
    def get_cardsuit(self):
        return self._suit

    # returns number of its instance as an accessor
    def get_number(self):
        return self._number

    # set the location of the card, if it moves for tracing purposes
    def set_location(self, location):
        self._location = location

    # this is a private method for validate the value of a card from the domain of 0 < x < 14
    def __is_valid(number):
        if number < 1 or number > 13 :
            # since I cannot use exception, I will use printing method
            print("You cannot create a card number more than 13")
            return False
        else:
            return True

