import random
import sys
import time
import copy
from math import inf

def initGrid(): #creates the 3x3 TicTacToe Board
    grid = []
    for i in range(3):
        row = []
        for i in range(3):
            row.append("[ ]")
        grid.append(row)
    return grid

def printGrid(list): #displays the board
    for i in range(len(list)):
        for j in range(len(list[0])):
            print(list[i][j], end = "")
        print("")

def twoInARow(list, val): #checks to see if there are 2 of the same value (X or O) in a row/vertical/diagonal
    #top row
    if (list[0][0] == list[0][1] and list[0][2] == "[ ]" and list[0][0] == val):
        list[0][2] = val
        return True
    if (list[0][2] == list[0][1] and list[0][0] == "[ ]" and list[0][2] == val):
        list[0][0] = val
        return True
    if (list[0][0] == list[0][2] and list[0][1] == "[ ]" and list[0][0] == val):
        list[0][1] = val
        return True
    #left edges
    if (list[0][0] == list[2][0] and list[1][0] == "[ ]" and list[0][0] == val):
        list[1][0] = val
        return True
    if (list[0][0] == list[1][0] and list[2][0] == "[ ]" and list[0][0] == val):
        list[2][0] = val
        return True
    if (list[1][0] == list[2][0] and list[0][0] == "[ ]" and list[1][0] == val):
        list[0][0] = val
        return True
    #right edges
    if (list[0][2] == list[1][2] and list[2][2] == "[ ]" and list[0][2] == val):
        list[2][2] = val
        return True
    if (list[0][2] == list[2][2] and list[1][2] == "[ ]" and list[0][2] == val):
        list[1][2] = val
        return True
    if (list[1][2] == list[2][2] and list[0][2] == "[ ]" and list[1][2] == val):
        list[0][2] = val
        return True
    #center vertical
    if (list[0][1] == list[1][1] and list[2][1] == "[ ]" and list[0][1] == val):
        list[2][1] = val
        return True
    if (list[0][1] == list[2][1] and list[1][1] == "[ ]" and list[0][1] == val):
        list[1][1] = val
        return True
    if (list[1][1] == list[2][1] and list[0][1] == "[ ]" and list[1][1] == val):
        list[0][1] = val
        return True
    #middle row
    if (list[1][0] == list[1][1] and list[1][2] == "[ ]" and list[1][0] == val):
        list[1][2] = val
        return True
    if (list[1][2] == list[1][1] and list[1][0] == "[ ]" and list[1][2] == val):
        list[1][0] = val
        return True
    if (list[1][0] == list[1][2] and list[1][1] == "[ ]" and list[1][0] == val):
        list[1][1] = val
        return True
    #bottom row
    if (list[2][0] == list[2][1] and list[2][2] == "[ ]" and list[2][0] == val):
        list[2][2] = val
        return True
    if (list[2][2] == list[2][1] and list[2][0] == "[ ]" and list[2][2] == val):
        list[2][0] = val
        return True
    if (list[2][0] == list[2][2] and list[2][1] == "[ ]" and list[2][0] == val):
        list[2][1] = val
        return True
    #diagonal left -> right
    if (list[0][0] == list[1][1] and list[2][2] == "[ ]" and list[0][0] == val):
        list[2][2] = val
        return True
    if (list[0][0] == list[2][2] and list[1][1] == "[ ]" and list[2][2] == val):
        list[1][1] = val
        return True
    if (list[2][2] == list[1][1] and list[0][0] == "[ ]" and list[1][1] == val):
        list[0][0] = val
        return True
    #diagonal right -> left
    if (list[2][0] == list[2][1] and list[0][2] == "[ ]" and list[2][0] == val):
        list[0][2] = val
        return True
    if (list[0][2] == list[1][1] and list[2][0] == "[ ]" and list[0][2] == val):
        list[2][0] = val
        return True
    if (list[2][0] == list[0][2] and list[1][1] == "[ ]" and list[0][2] == val):
        list[1][1] = val
        return True
    
    return False

def twoInARowBlock(list, val, player): #does the same as the function above, but checks the player's value to see if the computer can block
    #top row
    if (list[0][0] == list[0][1] and list[0][2] == "[ ]" and list[0][0] == player):
        list[0][2] = val
        return True
    if (list[0][2] == list[0][1] and list[0][0] == "[ ]" and list[0][2] == player):
        list[0][0] = val
        return True
    if (list[0][0] == list[0][2] and list[0][1] == "[ ]" and list[0][0] == player):
        list[0][1] = val
        return True
    #left edges
    if (list[0][0] == list[2][0] and list[1][0] == "[ ]" and list[0][0] == player):
        list[1][0] = val
        return True
    if (list[0][0] == list[1][0] and list[2][0] == "[ ]" and list[0][0] == player):
        list[2][0] = val
        return True
    if (list[1][0] == list[2][0] and list[0][0] == "[ ]" and list[1][0] == player):
        list[0][0] = val
        return True
    #right edges
    if (list[0][2] == list[1][2] and list[2][2] == "[ ]" and list[0][2] == player):
        list[2][2] = val
        return True
    if (list[0][2] == list[2][2] and list[1][2] == "[ ]" and list[0][2] == player):
        list[1][2] = val
        return True
    if (list[1][2] == list[2][2] and list[0][2] == "[ ]" and list[1][2] == player):
        list[0][2] = val
        return True
    #center vertical
    if (list[0][1] == list[1][1] and list[2][1] == "[ ]" and list[0][1] == player):
        list[2][1] = val
        return True
    if (list[0][1] == list[2][1] and list[1][1] == "[ ]" and list[0][1] == player):
        list[1][1] = val
        return True
    if (list[1][1] == list[2][1] and list[0][1] == "[ ]" and list[1][1] == player):
        list[0][1] = val
        return True
    #middle row
    if (list[1][0] == list[1][1] and list[1][2] == "[ ]" and list[1][0] == player):
        list[1][2] = val
        return True
    if (list[1][2] == list[1][1] and list[1][0] == "[ ]" and list[1][2] == player):
        list[1][0] = val
        return True
    if (list[1][0] == list[1][2] and list[1][1] == "[ ]" and list[1][0] == player):
        list[1][1] = val
        return True
    #bottom row
    if (list[2][0] == list[2][1] and list[2][2] == "[ ]" and list[2][0] == player):
        list[2][2] = val
        return True
    if (list[2][2] == list[2][1] and list[2][0] == "[ ]" and list[2][2] == player):
        list[2][0] = val
        return True
    if (list[2][0] == list[2][2] and list[2][1] == "[ ]" and list[2][0] == player):
        list[2][1] = val
        return True
    #diagonal left -> right
    if (list[0][0] == list[1][1] and list[2][2] == "[ ]" and list[0][0] == player):
        list[2][2] = val
        return True
    if (list[0][0] == list[2][2] and list[1][1] == "[ ]" and list[2][2] == player):
        list[1][1] = val
        return True
    if (list[2][2] == list[1][1] and list[0][0] == "[ ]" and list[1][1] == player):
        list[0][0] = val
        return True
    #diagonal right -> left
    if (list[2][0] == list[2][1] and list[0][2] == "[ ]" and list[2][0] == player):
        list[0][2] = val
        return True
    if (list[0][2] == list[1][1] and list[2][0] == "[ ]" and list[0][2] == player):
        list[2][0] = val
        return True
    if (list[2][0] == list[0][2] and list[1][1] == "[ ]" and list[0][2] == player):
        list[1][1] = val
        return True
    
    return False

def corners(list, val):
    if (list[0][0] == "[ ]"):
        list[0][0] = val
        return True
    if (list[2][0] == "[ ]"):
        list[2][0] = val
        return True
    if (list[2][2] == "[ ]"):
        list[2][2] = val
        return True
    if (list[0][2] == "[ ]"):
        list[0][2] = val
        return True
    
    return False

def centerGame(list, val):
    if (list[1][1] == "[ ]"):
        list[1][1] = val
        return True
    return False

def edges(list, val):
    if (list[1][0] == "[ ]"):
        list[1][0] = val
        return True
    if (list[0][1] == "[ ]"):
        list[0][1] = val
        return True
    if (list[2][1] == "[ ]"):
        list[2][1] = val
        return True
    if (list[1][2] == "[ ]"):
        list[1][2] = val
        return True
    
    return False

def threeInARow(list, val): #checks to see if there is a winner with 3 of a value in a row
    if (list[0][0] == list[0][1] and list[0][1] == list[0][2] and list[0][0] == val):
        return True
    if (list[1][0] == list[1][1] and list[1][1] == list[1][2] and list[1][0] == val):
        return True
    if (list[2][0] == list[2][1] and list[2][1] == list[2][2] and list[2][0] == val):
        return True
    if (list[0][0] == list[1][0] and list[1][0] == list[2][0] and list[0][0] == val):
        return True
    if (list[0][1] == list[1][1] and list[1][1] == list[2][1] and list[0][1] == val):
        return True
    if (list[0][2] == list[1][2] and list[1][2] == list[2][2] and list[0][2] == val):
        return True
    if (list[0][0] == list[1][1] and list[1][1] == list[2][2] and list[0][0] == val):
        return True
    if (list[0][2] == list[1][1] and list[1][1] == list[2][0] and list[2][0] == val):
        return True
    
    return False

def findDraw(list): #checks to see if the board is full
    for i in range(len(list)):
        for j in range(len(list[i])):
            if (list[i][j] == "[ ]"):
                return False
    return True

def playerChooses(list, val): #player's choice
    while True:
        r = int(input("Pick a row (0-2): "))
        c = int(input("Pick a column (0-2): "))
        if (r < 0 or r > 2 or c < 0 or c > 2):
            continue
        if (list[r][c] == "[ ]"):
            list[r][c] = val
            break
    printGrid(list)
    print(" ")
    if (threeInARow(list, val)):
        print("CONGRATS YOU WON")
        return True
    elif (findDraw(list)):
        return True
    return False

# Priorities:
#     if there are 2 in a row of its own value and the 3rd space is empty, place in that space
#     if there are 2 in a row of the opposing value and the third space is empty, block by placing there

#     find empty corner
#     start with center placement
#     start with edge

def computerChoosesRand(list, val): #random placement from the computer
    random.seed(a = None, version = 2)
    while True:
        comp_r = random.randint(0,2)
        comp_c = random.randint(0,2)
        if (list[comp_r][comp_c] == "[ ]"):
            # print("I will be placing here!")
            list[comp_r][comp_c] = val
            break

def computerChoosesAI(list, val, player): #has certain priorities that it follows to block you, or go for a win
    #2 in a row of own
    if (twoInARow(list, val)):
        return
    if (twoInARowBlock(list, val, player)):
        return
    if (corners(list, val)):
        return
    if (centerGame(list, val)):
        return
    
    edges(list, val)

def makeScore(list, depth, val, player):
    if (threeInARow(list, val)):
        return 1
    if (threeInARow(list, player)):
        return -1

    return 0



# def minimaxRecursive(list, depth, val, player):
#     if (threeInARow(list, val) or threeInARow(list, player)):
#         return [-1,-1,makeScore(list, depth, val, player)]
#     depth+=1
#     moveX = -1
#     moveY = -1
#     score = -2
#     for i in range(len(list)):
#         for j in range(len(list[i])):
#             if (list[i][j] == "[ ]"):
#                 newList = copy.   (list)
#                 if (depth%2 == 0):
#                     newList[i][j] = val
#                 else:
#                     newList[i][j] = player                    
#                 best = minimaxRecursive(newList, depth, val, player)
#                 copyScore = best[2]
#                 if ((copyScore > score and depth%2 == 0) or (copyScore < score and depth%2 != 0)):
#                     score = copyScore
#                     moveX = i
#                     moveY = j

    
#     return [moveX, moveY, score]

def minimaxRecursive(list, depth, comp, player, val): #main bulk of minimax algorithm, set recursively so that it can test each possible move
    if (val == 1):
        best = [-1,-1,-inf]
    else:
        best = [-1,-1,inf]
    if (depth == 0 or threeInARow(list, comp) or threeInARow(list, player)):
        if (threeInARow(list, comp)):
            score = 1
        elif (threeInARow(list, player)):
            score = -1
        else:
            score = 0
        return [-1,-1,score]
    for i in range(len(list)):
        for j in range(len(list[i])):
            if (list[i][j] == "[ ]"):
                if (val == 1):
                    list[i][j] = comp
                else:
                    list[i][j] = player
                copyScore = minimaxRecursive(list, depth-1, comp, player, -val)
                list[i][j] = "[ ]"
                copyScore[0] = i
                copyScore[1] = j
                if (val == 1 and copyScore[2] > best[2]):
                    best = copyScore
                elif (val != 1 and copyScore[2] < best[2]):
                    best = copyScore
    return best
    

def minimaxAI(list, val, player): #the unbeatable AI itself
    filled = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            if (list[i][j] != "[ ]"):
                filled+=1
    if (9-filled == 0 or threeInARow(list, val) or threeInARow(list, player)):
        return
    if (filled == 0):
        computerChoosesRand(list, val)
        return
    score = minimaxRecursive(list, 9-filled, val, player, 1)
    if (score[0] < 0 or score[1] < 0):
        computerChoosesRand(list, val)
    else:
        list[score[0]][score[1]] = val

def playGameEasy(list): #plays with random choice
    choice = ""
    computer = ""
    while True:
        choice = input("would you like to be Xs or Os? ")
        if (choice == "X" or choice == "x"):
            print("i shall play with O")
            computer = "[O]"
            choice = "[X]"
            break
        elif (choice == "O" or choice == "o"):
            print("i shall play with X")
            computer = "[X]"
            choice = "[O]"
            break
    while True:
        printGrid(list)
        print(" ")
        if (threeInARow(list, computer)):
            print("YOU LOST")
            break
        elif (findDraw(list)):
            print("IT'S A DRAW")
            break

        if(playerChooses(list, choice)):
            break
        computerChoosesRand(list, computer)

def playGameMedium(list): #plays with an AI that has certain priorities
    choice = ""
    computer = ""
    while True:
        choice = input("would you like to be Xs or Os? ")
        if (choice == "X" or choice == "x"):
            print("i shall play with O")
            computer = "[O]"
            choice = "[X]"
            break
        elif (choice == "O" or choice == "o"):
            print("i shall play with X")
            computer = "[X]"
            choice = "[O]"
            break
    while True:
        printGrid(list)
        print(" ")
        if (threeInARow(list, computer)):
            print("YOU LOST")
            break
        elif (findDraw(list)):
            print("IT'S A DRAW")
            break

        if(playerChooses(list, choice)):
            break
        computerChoosesAI(list, computer, choice)

def playGameHard(list): #plays game with minimax AI
    choice = ""
    computer = ""
    while True:
        choice = input("would you like to be Xs or Os? ")
        if (choice == "X" or choice == "x"):
            print("i shall play with O")
            computer = "[O]"
            choice = "[X]"
            break
        elif (choice == "O" or choice == "o"):
            print("i shall play with X")
            computer = "[X]"
            choice = "[O]"
            break
    while True:
        printGrid(list)
        print(" ")
        if (threeInARow(list, computer)):
            print("YOU LOST")
            break
        elif (findDraw(list)):
            print("IT'S A DRAW")
            break

        if(playerChooses(list, choice)):
            break
        minimaxAI(list, computer, choice)

def decision(): #allows player to choose difficulty
    while True:
        difficulty = int(input("How difficult do you want it? 0 for easy, 1 for medium,  and 2 for hard: "))
        if (difficulty == 0):
            playGameEasy(initGrid())
            break
        elif (difficulty == 1):
            playGameMedium(initGrid())
            break
        elif (difficulty == 2):
            playGameHard(initGrid())
            break
        else:
            print("Not applicable. Choose a number in between 0 and 2.")
            continue

def AITest(): #used to test certain AIs against each other (Priorities vs Random: AI won ~700/1000 times, Priorities vs Minimax: All Draws, Minimax vs Random: Minimax won all)
    aiWins = 0
    randWins = 0
    ties = 0
    choice = "[X]"
    computer = "[O]"
    for i in range(1000):
        print(i)
        list = initGrid()
        while True:
            if (threeInARow(list, computer)):
                aiWins +=1
                break
            elif (findDraw(list)):
                ties += 1
                break

            computerChoosesAI(list, choice, computer)
            # computerChoosesRand(list, computer)
            if (threeInARow(list, choice)):
                randWins+=1
                break
            minimaxAI(list, computer, choice)
        
    print("Minimax: ", aiWins)
    print("Priorities: ", randWins)
    print("Ties: ", ties)


# playGame(initGrid())
AITest()
# decision()

#Sources for Minimax learning
#https://towardsdatascience.com/tic-tac-toe-creating-unbeatable-ai-with-minimax-algorithm-8af9e52c1e7d
# https://github.com/Cledersonbc/tic-tac-toe-minimax/blob/master/py_version/minimax.py

# HERE!!!
# https://cs.stanford.edu/people/eroberts/courses/soco/projects/2003-04/intelligent-search/minimax.html
