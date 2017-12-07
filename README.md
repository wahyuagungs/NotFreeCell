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

There are 12 files with an extension of .py, and a package folder in this project. From those files, developer has created 10 classes and 2 modules. Some of the classes are base class and others are derived class from base class or an enum class. 
This application has 3 Enum classes, CardColor, CardSuit, and Color. They create a relationship by using other object as a field in another. For example, CardSuit has a property called CLUBS, which has a property from CardColor called BLACK, and that particular CardColor property has a property binary UTF-8 value of '\033[30m'. This allows developer to use existing value and can make the changes easier and become more agile in development stage.	   
 In addition to that, another set of classes that heavily use inheritance concept are Stack, Deck, Tableau and Foundation. Stack will become the base class among them, in terms that every child class can re-use or extend the usage of their parent’s method, making every change become more precise and verbose. For example, one of the methods inside Stack class is push() method, it allows a card object being stacked on top of the list of cards inside of its object. However, there are different logic or validation sets for every child classes implementation, one class might have to check its color and number, another will have to check only its suit and number. Eventually, for every successful validation will result a card be pushed on top of the object. Hence, a child class will invoke parent’s class method only after a card has been successfully validated.
To give more abstraction concept of every implementation, here are the classes inside this project.
1.	Color Class
This class uses enum as its base class, for constructing properties inside of its class that allows for any implementation to avoid any unnecessarily mistakes, or any code repetition. For example, to print a card, it will use a string value to represent a  colour. Other usage from other classes such as display boards of matrix can also use these properties values.
2.	CardColor Class
It will only have 2 properties comprises of BLACK and RED, both use Color Class enum as one of its value and an integer value to represent mathematical value of a colour. The latter allows mathematical operation by comparing the integer value of a colour inside of any cards. This integer value comprise of the number of 0 or 1 which represent the colour of RED and BLACK respectively. 
3.	CardSuit Class
This class uses 4 properties with 2 values each, to determine a face suit of a card. It also has four UTF symbols to denote a card in its manner. The goal is to give a better representation and user experience when the user wants to play the game. This class has 3 accessor methods to get some of its values such as colour name, colour value and the name of its instance. This class will be one of the arguments for another class such as Deck and Card class. 
4.	Card Class
This class is the core object of this game, every card object in this game will be instantiated distinctly with its number, face or suit, and colour. Inside a card, a number will be assigned for each card from 1 (Ace) to 13 (King). Every card has a face or suit that comprises of four types: diamonds, hearts, spades, and clubs. Therefore, there will be only 52-card given, ignoring the jokers. 
In addition, this class also has 3 arguments, which 2 of them are mandatory to determine a card’s number and suit. Its colour will be determined based on its suit since its suit will have only a colour. 
