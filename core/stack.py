# stack.py: implementation of the Stack ADT using an array structure
# Original created by Gavin Kroeger,and Jojo Wong
# This class will be modified appropriately for the needs of Not FreeCell Game
# http://moodle.vle.monash.edu/course/view.php?id=38153&section=11


class Stack:
    # creates a new stack
    # All private variables will be using single underscore name (PEP-8 Naming Convention Standard) e.g. self._count
    def __init__(self):
        self._cards = []  # represent the stack as a list
        self._count = 0  # indicate the current size of the stack
        self._top = -1  # indicate the top position of the stack
        self._iterator = iter(self._cards) # create iterator object protocol

    # returns the number of items in the stack
    def __len__(self):
        return self._count

    # returns True if the stack is empty or False otherwise
    def is_empty(self):
        return len(self) == 0

    # pushes an item onto the top of the stack
    def push(self, item):
        self._cards.append(item)
        self._top += 1
        self._count += 1

    # removes and returns the top item on the stack
    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        item = self._cards[self._top]
        self._top -= 1
        self._count -= 1
        del self._cards[len(self)]
        return item

    # returns the item on the stack without removing it
    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        item = self._cards[self._top]
        return item

    # this magic function will return an iterator protocol object instead of iterable object
    # So, it can be used directly inside for loop inside implementation method of a class
    def __iter__(self):
        for item in self._cards:
            yield item

    # format the output
    def __str__(self):
        for item in self._cards:
            item += ", "

    def get_cards(self):
        return self._cards

    # this method will add a collection of cards from the argument into card list using extend method
    # without removing existing objects
    def add_cards(self, cards):
        self._cards.extend(cards)
        self._count += len(cards)
        self._top += len(cards)

    # this method will add a card from the argument, into an existing card list resides within a deck object
    # I did this because, I have to put this in place and cannot change any existing method so, here it is.
    def add_card(self, card):
        self.push(card)
