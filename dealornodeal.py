# Name, Perm, Class, Date
# Deal or No Deal Game

# External Libraries
import random

# Global Variables
MONEY_FILE = "money.txt"

# Fix the Random State
#random.seed(255)

def parseFile(path):
    """
    Parse file of money values and stores the each value
    as an element of a list.
    
    :parameter path - path to file (string)
    :return lyst - list of all 26 money amounts (as floats)
    """
    lyst = list() #stub

    return lyst


def setUp(lyst):
    """
    Assigns a random, unique money amount to each case number
    ranging from 1 to 26, inclusive.

    :parameter lyst - list of all 26 money amounts (as floats)
    :return dyct - dictionary of {caseNumber : moneyAmount}
    (Note: caseNumber should be a string; moneyAmount should
    be a float.)
    """
    dyct = dict() #stub
        
    return dyct

def convertToBoard(lyst):
    """
    Converts the list remaining money amounts into a 2D list
    of remaining money amounts, with the lowest amounts of the
    left and the highest amounts on the right.

    :parameter lyst - list of remaining money amounts (as floats)
    (Note: money amounts that have been removed from the game
    are empty strings in the lyst paramter)
    :return board - 2D list of remaining money amounts
    """
    board = [] #stub
        
    return board

def outputBoard(board):
    """
    Outputs the current board state. 
    
    :parameter board - 2D list of remaining money amounts
    """

    return #stub

def getUserInput(lyst):
    """
    Prompts the user to choose a valid case number from the
    list of remaining cases that is not the chosen case.

    :parameter lyst - list of remaining unopened cases
    :return userInput - valid case number (integer)
    """
    userInput = -1 #stub

    return userInput

def openCase(dyct, lyst, num):
    """
    Opens one of the remaining cases, outputting to the user
    to inform them of the contents of the case. Replaces this
    money amount from the list of remaining money amounts with
    an empty string and removes this case from the remaining cases.

    :parameter dyct - dictionary of {caseNumber : moneyAmount}
    remaining. (Note: caseNumber should be a string; moneyAmount
    should be a float.)
    :parameter lyst - list of remaining money amounts (as floats)
    :parameter num - valid case number (string)
    (Note: the function does not need to return anything since
    the original list and dictionary will be modified due to
    their mutability property.)
    """
    
    return #stub

def expectation(dyct):
    """
    Calculates the expected value of the cases remaining.

    :parameter dyct - dictionary of {caseNumber : moneyAmount}
    remaining. (Note: caseNumber should be a string; moneyAmount
    should be a float.)
    :return num - expected value (float)
    """
    result = 0 #stub
            
    return result

def bankOffer(dyct):
    """
    Calculates the banker's offer based on a proportion
    of the expected value.

    :parameter dyct - dictionary of {caseNumber : moneyAmount}
    remaining. (Note: caseNumber should be a string; moneyAmount
    should be a float.)
    :return num - banker's offer (float)
    """
    num = 0 #stub
    
    return num

def startRound(dyct, lyst, caseNum, roundNum):
    """
    For rounds 1 through 9...
    Prompts the user to open a number of cases depending on the
    round. Once all the cases for a round has been opened,
    output the new board state. Then, output a banker offer.
    Prompt the user to either take the banker's deal or turn it
    away by saying 'no deal'.

    For round 10...
    Prompt the user to either keep their original case or swap
    with the other remaining case. Then, open the chosen case and
    display the user's winnings.

    :parameter dyct - dictionary of {caseNumber : moneyAmount}
    remaining. (Note: caseNumber should be a string; moneyAmount
    should be a float.)
    :parameter lyst - list of remaining money amounts (as floats)
    :parameter caseNum - chosen case from beginning of the game (str)
    :parameter roundNum - round number
    :return bool - return True if the user has accepted a banker
    offer OR the user has opened a case in the final round 
    """
    print("\n\nRound {} Starting...\n".format(roundNum))

    return True #stub

def startGame():
    """
    The main function to run operate a game of Deal or No Deal.
    """
    print("Welcome to Deal or No Deal!")
    print("Listed below are all the various cash prizes \
you could walk away with today!")

    #read money amounts
    moneyAmounts = parseFile(MONEY_FILE)

    #initial randomization of money amount
    cases = setUp(moneyAmounts)

    #initial output    
    outputBoard(convertToBoard(moneyAmounts))

    #get contestant's chosen case
    print("Start by choosing your lucky case...")
    chosenCase = getUserInput(list(cases.keys()))

    #call startRound( ) for up to 10 rounds, either until
    #a banker's offer is accepted OR all 10 rounds are played.

    '''You must implement this part'''
    
        
if __name__ == '__main__':
    startGame()
            
    
    
