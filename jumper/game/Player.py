import random
"""
Author: Alvaro Loran    
A class that handles the list of words and it's empty counterpart, picks the random word for the game from list,
and the logic behind comparing and updating the empty list with a guess.
    
The responsibility of a TerminalService is to receive input guess as a lowercase letter, 
determine if the guess is found in the word, 
provide a message for a missed guess while keeping track of number of missed guesses,
update and provide the updated list when a correct guess is entered.
"""

class Player:
    
    def __init__(self):

        # the word list item lenght is matched in the blank list by index. ex. wordList[1] is the same length as blanklist[1]
        self._wordList = [
            ["a","p","p","l","e"],
            ["p","y","t","h","o","n"],
            ["c","o","d","i","n","g"],
            ["c","a","t"],
            ["c","o","m","p","u","t","e","r"]
            ]
        self._blankList = [
            ["-","-","-","-","-"],
            ["-","-","-","-","-","-"],
            ["-","-","-","-","-","-"],
            ["-","-","-"],
            ["-","-","-","-","-","-","-","-"]
        ]
        #the word, wordIndex, and wordInList will get randomly assigned when pickWord() is called
        self._word = str
        self._wordIndex = -1
        #word in list form to be used to check guesses
        self._wordInList = list

        #will keep track of missed guesses, is updated when a wrong guess is entered into updateGuess()
        self._missedGuesses= 0


    """
    This method will pick a random word from the list of words set in __init__ 
    and update variables to be used by other methods in class
    """
    def pickWord (self):

        #gets random number from 0 to 4 to be used as the index in the list of words
        self._wordIndex = random.randint(0,4)

        #assign the word in list form based on the index generated, this will be used by other methods as well. ex. ["a","p","p","l","e"]
        self._wordInList = self._wordList[self._wordIndex]

        #turns the list of characters in wordInList variable to a regular string. ex. "apple". this will be used by later methods to determine if guess is correct.
        self._word = "".join(self._wordInList)



    #this method returns the current empty word in list form for the game (list)
    def getEmptyWord(self):
        return self._blankList[self._wordIndex]

    #this returs the current number of missed guesses (int)
    def getMissedGuesses(self):
        return self._missedGuesses


    """
    this method will receive a lower case letter guess,
    check for it in the word,
    update the empty list with the correct letter if the guess is correct,
    return a message if the guess is incorrect while keeping track of missed guesses 
    """
    def updateGuess(self,letterGuess):
        
        #check if the letter is found in the word
        if(letterGuess in self._word):
            #keep track of the current index
            index = -1
            #for loop iterating though the items in the wordInList (word in list form) to find where the letter appears
            for i in self._wordInList: 
                #keeps track of current index to update the blank list
                index+= 1
                if( i == letterGuess.lower()):
                    #updates the empty list with the correct guess in the correct index
                    self._blankList[self._wordIndex][index] = i
        #will return a message if the guess is incorrect and it will update the amount of missed guesses.
        else:
            self._missedGuesses += 1
            return("Letter not in word, try again!")






"""
THE FOLLOWING ARE EXAMPLES ON HOW TO INITIATE AND USE SOME METHODS IN THIS CLASS

player = Player()

player.pickWord()
player.updateGuess("p")

player.updateGuess("c")
"""