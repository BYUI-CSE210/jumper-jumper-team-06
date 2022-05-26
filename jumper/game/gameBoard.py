
# Displays the parachute and the man as separate lists. Pulls in the missed guesses
# to remove lines of parachute and returns the death image if required.
"""Written by Chris Kinne

Minor edits by Camden Chadsey"""

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

    # Logic that updates the parachute and man lists based on number of missed guesses
    def parachuteUpdate(self):
        if len(self._parachute) > 0:
            self._parachute.pop(0)
        else:
            self._man[0] = "  X  "
            
    # Loop that displays the parachute and the man in their active state
    def displayPerson(self):
        for i in range (len(self._parachute)):
            print(self._parachute[i])
        for j in range (len(self._man)):
            print(self._man[j])

    def loseCondition(self):
        if len(self._parachute) < 1:
            print("Oh no! You didn't make it!")
            return False
        else:
            return True