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
    
    file = open(path)
    lyst = list(map(float, file.read().split('\n')))
    file.close()

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

    duplicate = lyst.copy()
    random.shuffle(duplicate)
    
    for i in range(1, 27):
        dyct[str(i)] = duplicate[i-1]
        
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
    
    for i in range(13):
        board.append([lyst[i], lyst[i+13]])
        
    return board

def outputBoard(board):
    """
    Outputs the current board state. 
    
    :parameter board - 2D list of remaining money amounts
    """
    print("*" * 29)
    for row in board:
        left = row[0]
        right = row[1]
        if left != "":
            if left == 0.01:
                left = "$0.01"
            else:
                left = "${:,.0f}".format(left)
        if right != "":
            right = "${:,.0f}".format(right)
        print("**  {:>5}  **  {:>10}  **".format(left, right))
    print("*" * 29)

    return #stub

def getUserInput(lyst):
    """
    Prompts the user to choose a valid case number from the
    list of remaining cases that is not the chosen case.

    :parameter lyst - list of remaining unopened cases
    :return userInput - valid case number (integer)
    """
    userInput = -1 #stub
    
    while(userInput == -1):
        print("Remaining Cases: {}".format(lyst))
        userInput = input("Choose a case: ")
        if userInput in lyst:
            return userInput
        else:
            print("Invalid Choice. Choose again.\n")

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
    value = dyct.pop(num)
    lyst[lyst.index(value)] = ""

    if value == 0.01:
        print("Case {} contained... $0.01!\n".format(num))
    else:
        print("Case {} contained... ${:.0f}!\n".format(num, value))
    
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
    
    for value in dyct.values():
        if value != "":
            result += value
            
    return result / len(dyct)

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
    
    return ((26 - len(dyct)) / 24 + 0.01) * expectation(dyct)

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

    #Case for Round 10 (can separate into another function)
    if(roundNum == 10):
        response = input("Would you like to keep your case \
or swap with the other case remaining? ")
        while(response.lower() not in ["keep", "swap"]):
            print("Invalid Response. Try again.")
            response = input("Would you like to keep your case \
or swap with the other case remaining? ")
        
        if response.lower() == "keep":
            if dyct[caseNum] == 0.01:
                print("Case {} contains... $0.01!\n"
                      .format(caseNum))
                print("Congratulations! You have won $0.01!\n")
                      
            else:
                print("Case {} contains... ${:.0f}!\n"
                      .format(caseNum, dyct[caseNum]))
                print("Congratulations! You have won ${:.0f}!\n"
                      .format(dyct[caseNum]))
        else:
            remainingCases = list(dyct.keys())
            remainingCases.remove(caseNum)
            if remainingCases[0] == 0.01:
                print("Case {} contains... $0.01!"
                      .format(remainingCases[0]))
                print("Congratulations! You have won $0.01!\n")
            else:
                print("Case {} contains... ${:.0f}!"
                      .format(remainingCases[0],
                              dyct[remainingCases[0]]))
                print("Congratulations! You have won ${:.0f}!\n"
                      .format(dyct[remainingCases[0]]))
        return True

    #Case for other rounds
    #calculates number of cases to open
    if(roundNum < 6):
        casesToOpen = 7 - roundNum
    else:
        casesToOpen = 1

    #opens appropriate amount of cases
    for i in range(casesToOpen):
        remainingCases = list(dyct.keys())
        remainingCases.remove(caseNum)
        openCase(dyct, lyst, getUserInput(remainingCases))

    #outputs new state
    print("That's the end of Round {}.".format(roundNum))
    print("Let's look at the current board state:")
    outputBoard(convertToBoard(lyst))

    #banker offer
    print("The banker is offering you ${:.2f} to buy your case."
          .format(bankOffer(dyct)))
    
    #user response
    response = input("Deal or No Deal? ")
    while(response.lower() not in ["deal", "no deal"]):
        print("Invalid Response. Try again.")
        response = input("Deal or No Deal? ")
    
    if response.lower() == "deal":
        print("\nCongratulations! You have won ${:.2f}!"
              .format(bankOffer(dyct)))
        if dyct[caseNum] == 0.01:
            print("Your original case contained... $0.01!\n")
        else:
            print("Your original case contained... ${:.0f}!\n"
              .format(dyct[caseNum]))
        return True
    else:
        return False

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
    for i in range(1, 11):
        accepted = startRound(cases, moneyAmounts,
                                  chosenCase, i)
        if accepted:
            break
        
if __name__ == '__main__':
    startGame()
            
    
    
