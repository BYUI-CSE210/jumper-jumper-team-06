# Jumper
Starter template for the Jumper game
Update the readme with the rules for the game and the name of your team members.

Jumper Program Design

Rules
Jumper is played according to the following rules.

The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the game is over.
If the player has no more parachute the game is over.

Requirements
The program must also meet the following requirements.

The program must include a README file.
The program must include class and method comments.
The program must have at least four classes.
The program must remain true to game play described in the overview.


CLASSES:

	1.) Director 

		Responsibility:
			- Start the game. 
			- Direct the game events/sequence. 

		Behaviors:

			- handle random word
			- Display Blanks
			
			
			- GetInput()
			- doUpdates()
			- doOutputs()

		State:

			- (self) isPlaying
			- (self) startGame


	2.) TerminalService
		
		Responsibility:

			- Display game events to terminal.
			- Get user input/ push to director


		Behaviors:
			- read_text (gets text input from terminal)
			- write_text (displays given text on the terminal)

		State:
			- self 
			- prompt 


	3.) Player

	      Responsibility:

			- Will keep track of guess
			- will keep track of guess comparing

		Behaviors:

			- comunicate with GameBoard on how to modify output.
			- Determine if player is alive
			- Compare guess to the word dictionary


		State:
			- isPlayerAlive
			- guess		

	4.) GameBoard 


		Responsibility: 
			- Handle word lists
			- Updating word lists
			


		Behaviors:

			- Select word from list (random)
			- Store list (hard code)
			- Update list with player guess

		State:
			- Word list
			- Word variable
			- blanks List 
			

Assignments:

	GameBoard : Chris
	Player : Alvaro
	Director: Camden
	Terminal Service : Camden