from notfreecell import NotFreeCell


# this function is to validate input from the user
def input_validator(message, number=False, blank=False):
    val = input(message)
    if val.strip() == '' and not blank:
        print("You haven't type anything here")
        return input_validator(message, True)
    if number:
        if not val.isdigit():
            print("Your input is incorrect, Please type in numbers only")
            return input_validator(message, True)
        return int(val)
    else:
        return str(val)


def main():
    val_min = input_validator("Minimum value of a card : ", True)
    if val_min < 1 or val_min > 13:
        print("Invalid Number, only allowed from 1 - 13")
        main()

    val_max = input_validator("Maximum value of a card : ", True)
    if val_max < 1 or val_max > 13:
        print("Invalid Number, only allowed from 1 - 13")
        main()

    if val_max < val_min:
        print("Maximum value must be larger than minimum value")
        main()

    val_suit = input_validator("How many suits do you wanna play : ", True)
    if val_suit < 1:
        print("Minimum value for suit is 1")
        main()

    game = NotFreeCell(val_min, val_max, val_suit)
    game.display_board()
    play_game(game)


def play_game(game):
    source = input_validator("Source : ")
    destination = input_validator("Destination : ")
    game.move_card(source, destination)
    if not game.display_board():
        play_game(game)
    else:
        print("You have won the game !")


if __name__ == '__main__':
    print("Welcome to the NotFreeCell Game of Monash")
    print("To play this game, you can read wikipedia")
    main()
