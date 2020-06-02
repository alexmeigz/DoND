# Deal or No Deal

Deal or No Deal is a game show where a lucky player will get the chance to win a cash prize as large as $1,000,000. The game starts when the contestants selects 1 of the 26 cases, each holding a random cash value between $0.01 and $1,000,000. Then, the contestant will open a fixed amount of cases (depending on the round). After all the contestant has opened all the cases for the round, the banker will give the player a cash offer to buy their case. At this point, the player can sell their case for the amount the banker offered, or decline the offer and open several more cases. This will continue until there are two cases left. If an offer is declined when there are two cases left, then the contestant may choose to keep their case or swap their case with the other one remaining. The contestant wins the amount of money inside the case.

## Case Values

| Low | High |
| :---: | :---: |
| $0.01 | $ 1,000 |
| $1 | $ 5,000 |
| $5 | $ 10,000 |
| $10 | $ 25,000 |
| $25 | $ 50,000 |
| $50 | $ 75,000 |
| $75 | $ 100,000 |
| $100 | $ 200,000 |
| $200 | $ 300,000 |
| $300 | $ 400,000 |
| $400 | $ 500,000 |
| $500 | $ 750,000 |
| $750 | $1,000,000 |

## Game Overview
0. Contestant selects 1 case to keep for safekeeping.
1. Contestant opens 6 cases. (19 cases left.) Banker Offer follows. 
2. If offer is rejected, Contestant opens 5 more cases. (14 cases left.) Banker Offer follows. 
3. If offer is rejected, Contestant opens 4 more cases. (10 cases left.) Banker Offer follows. 
4. If offer is rejected, Contestant opens 3 more cases. (7 cases left.) Banker Offer follows. 
5. If offer is rejected, Contestant opens 2 more cases. (5 cases left.) Banker Offer follows. 
6. If offer is rejected, Contestant opens 1 more case. (4 cases left.) Banker Offer follows. 
7. If offer is rejected, Contestant opens 1 more case. (3 cases left.) Banker Offer follows. 
8. If offer is rejected, Contestant opens 1 more case. (2 cases left.) Banker Offer follows. 
9. If offer is rejected, Contestant opens 1 more case. (1 cases left.) Banker Offer follows. 
10. If offer is rejected, Contestant may keep their original case or swap with the 1 case left. They win amount described in chosen case.

## Implementation Guide
0. Download the starter files provided in this repository under the 'starter-files' directory. `dealornodeal.py` will contain the starter code and `money.txt` will contain the money values, each listed on a single line followed by a newline character.
Comments are listed in the starter code to explain the code itself.

1. Understand the global variables listed with the `if__name__ == '__main__':` block. We will be working with these variables extensively, passing them into functions for outputting and manipulation purposes.

2. Implement each of the following functions below, methodically, one-at-a-time. Test your functions to make sure that the inputs and outputs match the intended specification provided within the starter code itself.
    1. `parseFile()` 
    2. `setUp()`
    3. `convertToBoard()` 
    **Hint:** recall that lists and dictionaries have the mutability property and any changes we make to these structures within a function will make the change on the original copy. How could we leave the original copy untouched?
    4. `outputBoard()` 
    **Example:** for a full board with no removed values, see the output in Figure 1. 
    **Note:** there are 2 spaces separating the largest values of each column on either side and each row occupies exactly 28 characters. 
    **Hint:** recall the general format for a replacement field for string formatting {argumentIndex:spacesOccupied}. To specify that we want the comma thousands seperator, add a comma after the spacesOccupied parameter. To specify that we want n decimal points of precision, add .nf where n is a natural number after the spacesOccupied (and comma) parameter. (Note that the replacement field must be a float.) To specify alignment, add <, ^, or > before the spacesOccupiedParameter to left, center, or right justify respectively.
    5. `getUserInput()`
    **Example:** for an example call of `getUserInput()`, refer to Figure 2 below.
    6. `openCase()`
    **Example:** for an example call of `openCase()`, refer to Figure 3 below. (Note that the money amount may be different due to the random factor.)
    7. `expectation()`
    8. `bankOffer()`
    9. `startRound()`
    10. `startGame()`
     


Figure 1
```
****************************
**    $0  **      $1,000  **
**    $1  **      $5,000  **
**    $5  **     $10,000  **
**   $10  **     $25,000  **
**   $25  **     $50,000  **
**   $50  **     $75,000  **
**   $75  **    $100,000  **
**  $100  **    $200,000  **
**  $200  **    $300,000  **
**  $300  **    $400,000  **
**  $400  **    $500,000  **
**  $500  **    $750,000  **
**  $750  **  $1,000,000  **
****************************
```

Figure 2
```
Remaining Cases: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 100
Invalid Choice. Choose again.

Remaining Cases: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 1
```

Figure 3 (num = 1)
```
Case 1 contained... $50!
```

3. Confirm you are finished by calling the `startGame()` function within the `if__name__ == '__main__':` and playing a few games with different end conditions (accepting banker's offer, opening original case, etc.) until you are confident that the game is fully functional.
