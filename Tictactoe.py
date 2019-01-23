
#Tic_Tac_Toe.py
#Student assignment
#partially complete
#your work is indicated by comments **********
import random


#constants - but Python doesn't really have constants
EMPTY = " "
BAR = "|"
X = "X"
O = "O"


#functions    
def printInstructions():
    print("Tic Tac Toe")
    printDashes()
    print("You play first using X")
    print("Positions indexes begin with 1 (not 0)")
    print("The computer plays randomly using O")
    
def printDashes(n=30):
    DASH = "-"
    for i in range(n):
        print(DASH, end='')
    print()

def printTable(t):
    print()
    for row in range(3):
        for col in range(3):
            if col != 2:
                print(t[row][col], BAR, end='')
            else:
                print(t[row][col])
        if row != 2:
            printDashes(8)
    print()
        
def getPlayerMove():
    #********** needs improvement 
    #the player shouldn't be allowed to choose a position 
    #that's already occupied
    r = int(input("Row: "))
    c = int(input("Column: "))
        
    return r-1, c-1                 #so user understands not compsci real index

def getComputerMove(tbl):
    goodMove = False
    while goodMove == False:
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        if tbl[r][c] != X and tbl[r][c] != O:
            goodMove = True     
    return r, c
    
def recordPlayerMove(tbl, r, c):
    tbl[r][c] = X
    
def recordComputerMove(tbl, r, c):
    tbl[r][c] = O
    
def checkRow(tr, mark):
    for v in tr:
        if v != mark:
            return False
    return True

def checkCol(t, col, mark):
    for i in range(3):
        if t[i][col] != mark:
            return False
    return True

#********** define your diagonal checking here
    
def checkFor3s(tbl):
    #check rows
    if checkRow(tbl[0], X):
        return X
    if checkRow(tbl[1], X):
        return X
    if checkRow(tbl[2], X):
        return X
    if checkRow(tbl[0], O):
        return O
    if checkRow(tbl[1], O):
        return O
    if checkRow(tbl[2], O):
        return O
    #check columns
    if checkCol(tbl, 0, X):
        return X025
    if checkCol(tbl, 1, X):
        return X
    if checkCol(tbl, 2, X):
        return X
    if checkCol(tbl, 0, O):
            return O
    if checkCol(tbl, 1, O):
        return O
    if checkCol(tbl, 2, O):
        return O    
    #********** you need to write the function calls for checking 
    #columns for O
    
    #********** check diagonals
    #you need to write the function calls for checking diagonals
    #for X and O, and to define the function itself where
    #indicated above
    

    #no winner
    return None
    

#main part of the program
random.seed() #different sequence of randoms each run, so the
              #game plays differently every time

printInstructions()
table = [[EMPTY for i in range(3)] for i in range(3)]
printTable(table)
printDashes(60)
    
gameOver = False
while gameOver == False:
    print("Player move: ")
    r, c = getPlayerMove()
    recordPlayerMove(table, r, c) 
    printTable(table)
    
    print("Computer move: ")
    r, c = getComputerMove(table)
    recordComputerMove(table, r, c)
    printTable(table)
    
    winningPlayer = checkFor3s(table)
    #print("Winning player: ", winningPlayer) #use for debugging
    if winningPlayer == X:
        print("Congratulations, you won!")
        gameOver = True
    elif winningPlayer == O:
        print("Sorry, you lost to a stupid Python program!")
        gameOver = True
    else:
        print("No winner yet")
    printDashes(60)

        
        
        