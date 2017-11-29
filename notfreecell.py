from core.deck import Deck
from core.cell import Cell
from core.foundation import Foundation
from core.tableau import Tableau
from core.color import Color


# this class is the main implementation of NotFreeCell Game
class NotFreeCell:
    # instantiating objects related to the game
    def __init__(self, min_val=1, max_val=13, suit=4):
        self._deck = Deck(min_val, max_val, suit)
        self._cells = []  # creates list of cells
        self._tableaus = []  # creates list of tableaus
        self._foundations = []  # creates list of foundations
        self._matrix = []  # initial matrix list
        self._max_length = 0  # this will adjust based on the maximum length object of tableau

        # create 4 cells, n foundations and 8 tableaus objects
        # the number of foundation will have a default of 4 if the number of suit less than or equal to 4
        for i in range(0, 8):
            if i < 4:
                cell = Cell(i)
                self._cells.append(cell)
                foundation = Foundation(i)
                self._foundations.append(foundation)
            tableau = Tableau(i)
            self._tableaus.append(tableau)

        # if the number of suit more than 4, the number of foundation will follow
        i = 4
        while i < suit:
            foundation = Foundation(i)
            self._foundations.append(foundation)
            i += 1
        self._deck.shuffle_card()
        self.distribute_card()

    def distribute_card(self):
        # put from left to right one by one until its finished
        i = 0
        length = len(self._deck)  # get the length of stack objects
        while i < length:  # len(self._deck) cannot be placed here, because it'll evaluated for every increment of i
            item = self._deck.pop()
            m = i % 8  # Using modulus 8 to have co-domain result of (0 - 7) from any arbitrary domain
            item.set_location(i)
            self._tableaus[m].add_card(item, True)
            i += 1

    # This is a static method to return value that represent null, and avoid any error
    @staticmethod
    def val(li, idx):
        return li[idx] if len(li) > idx else Color.NEUTRAL.value + "-:-" + Color.NEUTRAL.value

    # returns tableaus objectlist
    def get_tableaus(self):
        return self._tableaus

    # returns foundations list
    def get_foundations(self):
        return self._foundations

    # returns cells list
    def get_cells(self):
        return self._cells

    # this method receive arguments to move a card object from one object container to other object container
    def move_card(self, source, destination):
        try:
            assert not source == destination, "Cannot move card to the same place"
            source_name = source[:1].upper()  # gets the first character only
            source_no = int(source[1:]) - 1  # removes the first character
            assert not source_no > 8 or source_no < 1, "Choose from Tableau Number 1 - 8"
            dest_name = destination[:1].upper()
            dest_no = int(destination[1:]) - 1
            assert not dest_no > 8 or dest_no < 1, "Choose from Tableau Number 1 - 8"
            if source_name == 'T':
                s_tab = self._tableaus[source_no]
                if dest_name == 'T':
                    d_tab = self._tableaus[dest_no]
                    d_tab.add_card(s_tab.peek())
                    s_tab.pop()
                elif dest_name == 'F':
                    d_fou = self._foundations[dest_no]
                    d_fou.add_card(s_tab.peek())
                    s_tab.pop()
                elif dest_name == 'C':
                    d_cel = self._cells[dest_no]
                    d_cel.add_card(s_tab.peek())
                    s_tab.pop()
                else:
                    raise Exception("You cannot move the card")
            elif source_name == 'F':
                s_fou = self._foundations[source_no]
                if dest_name == 'T':
                    d_tab = self._tableaus[dest_no]
                    d_tab.add_card(s_fou.peek())
                    s_fou.pop()
                elif dest_name == 'C':
                    d_cel = self._cells[dest_no]
                    d_cel.add_card(s_fou.peek())
                    s_fou.pop()
                elif dest_name == 'F':
                    d_fou = self._foundations[dest_no]
                    d_fou.add_card(s_fou.peek())
                    s_fou.pop()
                else:
                    raise Exception("You cannot move the card")
            elif source_name == 'C':
                s_cel = self._cells[source_no]
                if dest_name == 'T':
                    d_tab = self._tableaus[dest_no]
                    d_tab.add_card(s_cel.peek())
                    s_cel.pop()
                elif dest_name == 'F':
                    d_fou = self._foundations[dest_no]
                    d_fou.add_card(s_cel.peek())
                    s_cel.pop()
                elif dest_name == 'C':
                    d_cel = self._cells[dest_no]
                    d_cel.add_card(s_cel.peek())
                    s_cel.pop()
                else:
                    raise Exception("You cannot move the card")
            else:
                raise Exception("You choose the wrong letter buddy")
        except AssertionError as error:
            print(error)
        except Exception as error:
            print(error)

    # this will print the winning announcement
    def display_win_board(self):
        print("Congratulation, you have won this game !!!")

    # this method will construct matrix and display it in terminal
    def display_board(self):
        is_win = self.__construct_matrix()
        if not is_win:
            # self.__construct_headers()
            print('===' * 20)
            print(self.__construct_headers())
            print(self.__construct_upperlabel())
            print('---' * 20)
            print(self.__print_matrix())
            print(self.__construct_lowerlabel())
            print('---' * 20)
        return is_win

    def __construct_matrix(self):

        self._matrix = []
        # compare the length of each tableau
        # find maximum length for each tableau and store it to self._max_length
        self._max_length = max(len(card) for card in self._tableaus)

        #  this implies that all of the cards in tableaus have been gone to foundation
        #  and no cards in free cells
        if all(len(card) == 0 for card in self._tableaus) and \
                all(cell.is_empty() for cell in self._cells):
            self.display_win_board()
            return True

        # use the max_length to maximize the loop
        i = 0
        while i < self._max_length:
            self._matrix.append(['-:-'] * 8)
            for r in range(0, 8):
                item = self._tableaus[r].get_cards()
                self._matrix[i][r] = self.val(item, i)
            i += 1
        return False

    # returns upper section of matrix game board
    def __construct_headers(self):
        # list comprehension of join based on the number of cells and foundations
        cells = ' \t'.join(list(str(cell) for cell in self._cells))
        foundations = ' \t'.join(list(str(foundation) for foundation in self._foundations))
        return cells + ' \t' + foundations

    # returns upper labels
    def __construct_upperlabel(self):
        # list comprehension of join based on the number of cells and foundations
        cell = list('[C{}]'.format(c.get_location() + 1) for c in self._cells)
        foundation = list('[F{}]'.format(c.get_location() + 1) for c in self._foundations)
        return Color.NEUTRAL.value + ' \t'.join(cell) + ' \t' + ' \t'.join(foundation) + Color.NEUTRAL.value

    # Referenced from Monash Moodle  http://moodle.vle.monash.edu/course/view.php?id=38153&section=13
    def __print_matrix(self):
        new_string = ""
        for row in self._matrix:
            for item in row:
                new_string += str(item) + " \t"
            new_string.strip('\t')
            new_string += "\n"
        return new_string

    # returns lower labels
    def __construct_lowerlabel(self):
        return (Color.NEUTRAL.value + '[T1]' + ' \t' + '[T2]' + ' \t' + '[T3]' + ' \t' + '[T4]' + ' \t' +
                '[T5]' + ' \t' + '[T6]' + ' \t' + '[T7]' + ' \t' + '[T8]' + Color.NEUTRAL.value)
