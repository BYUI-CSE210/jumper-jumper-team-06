"""
Edited by Camden Chadsey
"""



"""Importing classes"""
from game.terminal_service import TerminalService
from game.Player import Player
from game.gameBoard import GameBoard

"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/encapsulation/materials/jumper-specification.html
"""


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._player = Player()
        self._game_board = GameBoard()
        self._playerGuess = " "
        self._outcome = True
        self._winCondition = False

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        #picking word with function from player class
        self._player.pickWord()

        #the main loop.
        while self._is_playing:
            
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """
        #checks for "is_playing" and "winCondition".
        if self._is_playing and not self._winCondition:
            #displays the blank list from player class
            self._player.displayBlankList()
            #displays the "man" and "parachute" from the gameboard class
            self._game_board.displayPerson()
            #gets input from the user with the terminal service class
            self._playerGuess = self._terminal_service.read_text("What letter do you guess?")
        
        #if successful win condition, congradulates user.
        elif self._is_playing and self._winCondition:
            self._game_board.displayPerson()
            print("You landed safely!")
        
        #otherwise you've lost. and it tells you that.
        else:
            self._game_board.displayPerson()
            print("You lost.")



    def _do_updates(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """
       #checks to see if player guessed correctly.
        self._outcome = self._player.updateGuess(self._playerGuess)

        #if they didnt, tell them so. 
        if not self._outcome:
            self._game_board.parachuteUpdate()
            print("Oh no! That was incorrect!")
            #resets the outcome variable.
            self._outcome = True
        
        #if they guessed right, tell them. then check to see if they won yet.
        else:
            print("You got it!")
            self._winCondition = self._player.winCondition()


    def _do_outputs(self):
        """Update this comment

        Args:
            self (Director): An instance of Director.
        """
        #checks to see if user lost.
        self._is_playing = self._game_board.loseCondition()


        