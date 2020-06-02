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

1. Implement each of the following functions below, methodically, one-at-a-time. Test your functions to make sure that the inputs and outputs match the intended specification provided within the starter code itself.
    1. `parseFile()` 
    2. `setUp()`
    3. `convertToBoard()` 
    **Hint:** recall that lists and dictionaries have the mutability property and any changes we make to these structures within a function will make the change on the original copy. How could we leave the original copy untouched?
    4. `outputBoard()` 
    **Example:** for a full board with no removed values, see the output in Figure 1. 
    **Note:** there are 2 spaces separating the largest values of each column on either side and each row occupies exactly 29 characters. 
    **Hint:** recall the general format for a replacement field for string formatting {argumentIndex:spacesOccupied}. To specify that we want the comma thousands seperator, add a comma after the spacesOccupied parameter. To specify that we want n decimal points of precision, add .nf where n is a natural number after the spacesOccupied (and comma) parameter. (Note that the replacement field must be a float.) To specify alignment, add <, ^, or > before the spacesOccupiedParameter to left, center, or right justify respectively.
    5. `getUserInput()`
    **Example:** for an example call of `getUserInput()`, refer to Figure 2 below.
    6. `openCase()`
    **Example:** for an example call of `openCase()`, refer to Figure 3 below. (Note that the money amount may be different due to the random factor.)
    7. `expectation()` 
    **Note:** expected value = sum of remaining money amounts / number of remaining cases.
    8. `bankOffer()`
    **Note:** banker offer = expected value of remaining cases * ((26 - number of remaining cases) / 24 + 0.01).
    9. `startRound()`
    **Example:** for an example call of `startRound()`, refer to Figure 4 below. (Note that the money amounts may be different due to the random factor.)
    10. `startGame()`
    **Example:** for a full example call of `startGame()`, refer to Figure 5 below. Make sure `random.seed()` is set to 255 to get the same results as the example below.

<details>
    <summary> Figure 1 </summary>
```
*****************************
**  $0.01  **      $1,000  **
**     $1  **      $5,000  **
**     $5  **     $10,000  **
**    $10  **     $25,000  **
**    $25  **     $50,000  **
**    $50  **     $75,000  **
**    $75  **    $100,000  **
**   $100  **    $200,000  **
**   $200  **    $300,000  **
**   $300  **    $400,000  **
**   $400  **    $500,000  **
**   $500  **    $750,000  **
**   $750  **  $1,000,000  **
*****************************
```
</details>

<details>
    <summary> Figure 2 </summary>
    
```
Remaining Cases: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 100
Invalid Choice. Choose again.

Remaining Cases: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 1

```
</details>

<details>
    <summary> Figure 3 </summary>
    
```
Case 1 contained... $50!


```
</details>

<details>
    <summary> Figure 4 </summary>
    
```


Round 1 Starting...

Remaining Cases: ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 2
Case 2 contained... $750000!

Remaining Cases: ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 3
Case 3 contained... $75!

Remaining Cases: ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 4
Case 4 contained... $400000!

Remaining Cases: ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 5
Case 5 contained... $50000!

Remaining Cases: ['6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 6
Case 6 contained... $0.01!

Remaining Cases: ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 7
Case 7 contained... $10!

That's the end of Round 1.
Let's look at the current board state:
*****************************
**         **      $1,000  **
**     $1  **      $5,000  **
**     $5  **     $10,000  **
**         **     $25,000  **
**    $25  **              **
**    $50  **     $75,000  **
**         **    $100,000  **
**   $100  **    $200,000  **
**   $200  **    $300,000  **
**   $300  **              **
**   $400  **    $500,000  **
**   $500  **              **
**   $750  **  $1,000,000  **
*****************************
The banker is offering you $28838.30 to buy your case.
Deal or No Deal? n
Invalid Response. Try again.
Deal or No Deal? deal

Congratulations! You have won $28838.30!
Your original case contained... $50!


```
</details>

<details>
    <summary> Figure 5 </summary>

```
Welcome to Deal or No Deal!
Listed below are all the various cash prizes you could walk away with today!
*****************************
**  $0.01  **      $1,000  **
**     $1  **      $5,000  **
**     $5  **     $10,000  **
**    $10  **     $25,000  **
**    $25  **     $50,000  **
**    $50  **     $75,000  **
**    $75  **    $100,000  **
**   $100  **    $200,000  **
**   $200  **    $300,000  **
**   $300  **    $400,000  **
**   $400  **    $500,000  **
**   $500  **    $750,000  **
**   $750  **  $1,000,000  **
*****************************
Start by choosing your lucky case...
Remaining Cases: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 1


Round 1 Starting...

Remaining Cases: ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 2
Case 2 contained... $750000!

Remaining Cases: ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 3
Case 3 contained... $75!

Remaining Cases: ['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 4
Case 4 contained... $400000!

Remaining Cases: ['5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 5
Case 5 contained... $50000!

Remaining Cases: ['6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 6
Case 6 contained... $0.01!

Remaining Cases: ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 7
Case 7 contained... $10!

That's the end of Round 1.
Let's look at the current board state:
*****************************
**         **      $1,000  **
**     $1  **      $5,000  **
**     $5  **     $10,000  **
**         **     $25,000  **
**    $25  **              **
**    $50  **     $75,000  **
**         **    $100,000  **
**   $100  **    $200,000  **
**   $200  **    $300,000  **
**   $300  **              **
**   $400  **    $500,000  **
**   $500  **              **
**   $750  **  $1,000,000  **
*****************************
The banker is offering you $28838.30 to buy your case.
Deal or No Deal? n
Invalid Response. Try again.
Deal or No Deal? no deal


Round 2 Starting...

Remaining Cases: ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 8
Case 8 contained... $1000!

Remaining Cases: ['9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 9
Case 9 contained... $100000!

Remaining Cases: ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 10
Case 10 contained... $10000!

Remaining Cases: ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 11
Case 11 contained... $5!

Remaining Cases: ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 12
Case 12 contained... $100!

That's the end of Round 2.
Let's look at the current board state:
*****************************
**         **              **
**     $1  **      $5,000  **
**         **              **
**         **     $25,000  **
**    $25  **              **
**    $50  **     $75,000  **
**         **              **
**         **    $200,000  **
**   $200  **    $300,000  **
**   $300  **              **
**   $400  **    $500,000  **
**   $500  **              **
**   $750  **  $1,000,000  **
*****************************
The banker is offering you $65792.28 to buy your case.
Deal or No Deal? no deal


Round 3 Starting...

Remaining Cases: ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 13
Case 13 contained... $300!

Remaining Cases: ['14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 14
Case 14 contained... $300000!

Remaining Cases: ['15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 15
Case 15 contained... $5000!

Remaining Cases: ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 16
Case 16 contained... $750!

That's the end of Round 3.
Let's look at the current board state:
*****************************
**         **              **
**     $1  **              **
**         **              **
**         **     $25,000  **
**    $25  **              **
**    $50  **     $75,000  **
**         **              **
**         **    $200,000  **
**   $200  **              **
**         **              **
**   $400  **    $500,000  **
**   $500  **              **
**         **  $1,000,000  **
*****************************
The banker is offering you $103976.98 to buy your case.
Deal or No Deal? no deal


Round 4 Starting...

Remaining Cases: ['17', '18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 17
Case 17 contained... $200!

Remaining Cases: ['18', '19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 18
Case 18 contained... $25000!

Remaining Cases: ['19', '20', '21', '22', '23', '24', '25', '26']
Choose a case: 19
Case 19 contained... $25!

That's the end of Round 4.
Let's look at the current board state:
*****************************
**         **              **
**     $1  **              **
**         **              **
**         **              **
**         **              **
**    $50  **     $75,000  **
**         **              **
**         **    $200,000  **
**         **              **
**         **              **
**   $400  **    $500,000  **
**   $500  **              **
**         **  $1,000,000  **
*****************************
The banker is offering you $168715.35 to buy your case.
Deal or No Deal? no deal


Round 5 Starting...

Remaining Cases: ['20', '21', '22', '23', '24', '25', '26']
Choose a case: 20
Case 20 contained... $500!

Remaining Cases: ['21', '22', '23', '24', '25', '26']
Choose a case: 21
Case 21 contained... $1000000!

That's the end of Round 5.
Let's look at the current board state:
*****************************
**         **              **
**     $1  **              **
**         **              **
**         **              **
**         **              **
**    $50  **     $75,000  **
**         **              **
**         **    $200,000  **
**         **              **
**         **              **
**   $400  **    $500,000  **
**         **              **
**         **              **
*****************************
The banker is offering you $108993.95 to buy your case.
Deal or No Deal? no deal


Round 6 Starting...

Remaining Cases: ['22', '23', '24', '25', '26']
Choose a case: 22
Case 22 contained... $75000!

That's the end of Round 6.
Let's look at the current board state:
*****************************
**         **              **
**     $1  **              **
**         **              **
**         **              **
**         **              **
**    $50  **              **
**         **              **
**         **    $200,000  **
**         **              **
**         **              **
**   $400  **    $500,000  **
**         **              **
**         **              **
*****************************
The banker is offering you $123979.83 to buy your case.
Deal or No Deal? no deal


Round 7 Starting...

Remaining Cases: ['23', '24', '25', '26']
Choose a case: 23
Case 23 contained... $500000!

That's the end of Round 7.
Let's look at the current board state:
*****************************
**         **              **
**     $1  **              **
**         **              **
**         **              **
**         **              **
**    $50  **              **
**         **              **
**         **    $200,000  **
**         **              **
**         **              **
**   $400  **              **
**         **              **
**         **              **
*****************************
The banker is offering you $46437.81 to buy your case.
Deal or No Deal? no deal


Round 8 Starting...

Remaining Cases: ['24', '25', '26']
Choose a case: 24
Case 24 contained... $200000!

That's the end of Round 8.
Let's look at the current board state:
*****************************
**         **              **
**     $1  **              **
**         **              **
**         **              **
**         **              **
**    $50  **              **
**         **              **
**         **              **
**         **              **
**         **              **
**   $400  **              **
**         **              **
**         **              **
*****************************
The banker is offering you $145.57 to buy your case.
Deal or No Deal? no deal


Round 9 Starting...

Remaining Cases: ['25', '26']
Choose a case: 25
Case 25 contained... $400!

That's the end of Round 9.
Let's look at the current board state:
*****************************
**         **              **
**     $1  **              **
**         **              **
**         **              **
**         **              **
**    $50  **              **
**         **              **
**         **              **
**         **              **
**         **              **
**         **              **
**         **              **
**         **              **
*****************************
The banker is offering you $25.75 to buy your case.
Deal or No Deal? no deal


Round 10 Starting...

Would you like to keep your case or swap with the other case remaining? s
Invalid Response. Try again.
Would you like to keep your case or swap with the other case remaining? swap
Case 26 contains... $1!
Congratulations! You have won $1!

```
</details>


2. Confirm you are finished by calling the `startGame()` function within the `if__name__ == '__main__':` and playing a few games with different end conditions (accepting banker's offer, opening original case, etc.) until you are confident that the game is fully functional.
