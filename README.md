# NotFreeCell
This project is part of my assignment while studying Python in Monash University. 

All right reserved.
This project uses a module called main.py as a controller to play the game, and a controller class named notfreecell.py to control the interface.
As part of our assignment, we were given a task to create a game that similar to FreeCell game but in different flavours according to the specifications.
Application will take several inputs as follows:
A minimum value of a card, a maximum value of a card, and the number of suit that are going to be played. However, due to the nature of the card themselves, there are several restrictions when a player wants to play this game. They are as follows:
1.	The value of a card can be in the domain of number 1 to 13, in which number 1 will be represent an ace and 11, 12, 13 will be Jack, Queen, and King of a suit respectively.
2.	Maximum value cannot be smaller than minimum value.
3.	Due to maintain the nature of this game, for every number of suit that less than 4, the number of foundations will still be 4. Whereas, the number of foundations will the same with the number of suits for every number of suits more than 4.
4.	This game will end by itself, and give the user information provided all of the cards have been placed gracefully into every available foundation.
Application will have to have a series of validation features according to https://en.wikipedia.org/wiki/FreeCell, some of them are as follows:
1.	Foundation: only an Ace of every suit can be placed for the first time or at the bottom of the foundation. Moreover, only the sequential number can be placed accordingly until reach the end of appropriate suit.
2.	Cells: Every card can be placed in the free cell, however once a card has been placed from either foundation or tableau, it cannot have another card being pushed. Because, a free cell can only contain a card at a time.
3.	Tableaus: Every tableau has the characteristics of a stack ADT object which uses Last in First Out concept. They will validate for every movement from others such as other tableaus, foundations, or even cells. For every card that will be placed, it cannot have the same card colour from its stack and must have a different number of one from its stack.
However, there are some general assumptions for using this game, they are as follows:
1.	No time limit constraint;
2.	A player cannot create a new game while the game is still in play;
3.	The movement of a card can only use the source and destination input.
