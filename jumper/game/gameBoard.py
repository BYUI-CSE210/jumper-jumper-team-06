from game.Player import Player

# Displays the parachute and the man as separate lists. Pulls in the missed guesses
# to remove lines of parachute and returns the death image if required.
class GameBoard:
    
    #Creates and instance of gameBoard
    def __init__(self):
        
        # List that defines the parachute life count.
        self._parachute = [
            " ___ ",
            "/___\ ",
            "\   /",
            " \ /"
        ]

        # List that defines the man and his life status.
        self._man = [
            "  0  ",
            " /|\ ",
            " / \ "
        ]

        # Pulls in the number of missed guesses from the Player class
        self._missedGuesses = player._missedGuesses()

    # Logic that updates the parachute and man lists based on number of missed guesses
    def parachuteUpdate(self):
        if self._parachute > 0:
            self._parachute.pop(0)
        else:
            self._man[0] = "  X  "
            return self._man 
            
    # Loop that displays the parachute and the man in their active state
    def displayPerson(self):
        for i in range (len(self._parachute)):
            print(self._parachute[i])
        for j in range (len(self._man)):
            print(self._man[j])