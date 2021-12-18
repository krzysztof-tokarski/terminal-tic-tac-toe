#!/usr/bin/env python
# coding: utf-8

# In[10]:


def whitespace():
    print("\n")


# In[47]:
# VALUES [NOT SURE IF ALL]

    global player_one
    global player_two
    global first
    global second
    global row1
    global row2
    global row3
    global moveset

    player_one = "X"
    player_two = None
    first = "X"
    second = "O"
    
    row1 = "|   |   |   |"
    row2 = "|   |   |   |"
    row3 = "|   |   |   |"
    
    moveset = {"1":row1[2],"2":row1[6],"3":row1[10],"4":row2[2],"5":row2[6],"6":row2[10],"7":row3[2],"8":row3[6],"9":row3[10]}


def reset_values():
    
    global player_one
    global player_two
    global first
    global second
    global row1
    global row2
    global row3
    
    player_one = None
    player_two = None
    first = None
    second = None
    
    row1 = "|   |   |   |"
    row2 = "|   |   |   |"
    row3 = "|   |   |   |"
    
    moveset = {"1":row1[2],"2":row1[6],"3":row1[10],"4":row2[2],"5":row2[6],"6":row2[10],"7":row3[2],"8":row3[6],"9":row3[10]}

#Input position are: [2,6,10]

def three_rows():
    print(row1)
    print(row2)
    print(row3)

def welcome():
    
    import random
    
    reset_values()
    
    print("Welcome to Tic Tac Toe.")
    
    whitespace()
    
    print('''RULES FOR TIC-TAC-TOE.\n\n1. The game is played on a grid that's 3 squares by 3 squares.\n2. One player chooses it's marker, either X or O, what determines marker of the other player.\n3. Then the game rolls who goes first.\n4. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n5. When all 9 squares are full, the game is over.''')
    
    whitespace()
    
    print("The board is organised as follows:")
    
    whitespace()
    
    print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")
    
    whitespace()
    
    print("How to indicate where you want to place your marker on the board?\nYou will have to indicate the desired position by referring to one of the above numbers.")
    
    whitespace()


# In[51]:


def display_board():
    
    print("Here's the current board:")
    
    whitespace()
    
    three_rows()

# In[11]:


def marker_designation():
    
    reset_values()
    
    markers = ["X","O","x","o"]
    
    while player_one not in markers:
        
        player_one = input("Choose your marker (X or O): ")
        
        if player_one not in markers:
            print("Ooops, something went wrong. Please try again.")
        
        if player_one == "X":
            player_one = "X"
            player_two = "O"
        
        if player_one == "x":
            player_one = "X"
            player_two = "O"

        if player_one == "o":
            player_one = "O"
            player_two = "X"
        
        if player_one == "O":
            player_one = "O"
            player_two = "X"

    whitespace()
    
    print(f"Player 1 shall play as {player_one} and Player 2 shall play as {player_two}.")


# In[22]:


def who_goes_first():
    
    import random
    
    global first
    global second
    
    global player_one 
    global player_two
    
    values = ["X","O"]
    
    first = random.choice(values)
    
    if first == player_one:
        print(f'Player 1 (playing as {player_one}) will go first.')
    if player_two == first:
        print (f'Player 2 (playing as {player_two}) will go first.')
    if first == "X":
        second = "O"
    if first == "O":
        second = "X"


# In[50]:


#Input position are: [2,6,10]

def win_condition():
    
    whitespace()
    
    global first
    global second
    
    global player_one 
    global player_two
    
    global row1
    global row2
    global row3
    
    row1 = [char for char in row1]
    row2 = [char for char in row2]
    row3 = [char for char in row3]
    
    transit1 = ''
    transit2 = ''
    transit3 = ''

    
    WinFlatOne = [row1[2], row1[6], row1[10]]
    WinFlatTwo = [row2[2], row2[6], row2[10]]
    WinFlatTree= [row3[2], row3[6], row3[10]]
    
    WinUpOne = [row1[2],row2[2],row3[2]]
    WinUpTwo = [row1[6],row2[6],row3[6]]
    WinUpTre = [row1[10],row2[10],row3[10]]
    
    WinDiagR = [row1[2],row2[6], row3[10]]
    WinDiagL = [row1[10],row2[6], row3[2]]
    
    WinCondition = [WinFlatOne,WinFlatTwo,WinFlatTree,WinUpOne,WinUpTwo,WinUpTre,WinDiagR,WinDiagL]
    
    for sublist in WinCondition:
        if sublist[0] == sublist[1] == sublist[2] == player_one:
            print(f'Player 1 is the winner! There are three {player_one} in a row!')
        if sublist[0] == sublist[1] == sublist[2] == player_two:
            print(f'Player 2 is the winner! There are three {player_two} in a row!')
            
    row1 = transit1.join(row1)
    row2 = transit2.join(row2)
    row3 = transit3.join(row3)
    
    whitespace()


def first_move():
    
    whitespace()
    
    global first
    global second
    
    global player_one 
    global player_two
    
    global row1
    global row2
    global row3
    
    global moveset
    
    first_move = None
    retired = []
    
    transit = ''
    
    #ROWS TO LISTS AND BACK TO STRINGS
    
    original_moveset = {"1":row1[2],"2":row1[6],"3":row1[10],"4":row2[2],"5":row2[6],"6":row2[10],"7":row3[2],"8":row3[6],"9":row3[10]}
    
    while first_move not in retired:
        first_move = input(f"Choose where on the board you want to place {first}: ")
        if first_move not in original_moveset:
            print("Sorry, I do not understand what you want to do, please try again.") 
            whitespace()
        if first_move not in moveset and first_move in original_moveset:
            print("Sorry, this position is already taken.")
            whitespace()
        if first_move in moveset:
            if first_move == "1":
                row1 = [char for char in row1]
                row1[2] = first
                row1 = transit.join(row1)
                retired.append(first_move)
                moveset.pop(first_move)
            if first_move == "2":
                row1 = [char for char in row1]
                row1[6] = first
                row1 = transit.join(row1)
                retired.append(first_move)
                moveset.pop(first_move)
            if first_move == "3":
                row1 = [char for char in row1]
                row1[10] = first
                row1 = transit.join(row1)
                retired.append(first_move)
                moveset.pop(first_move)
            if first_move == "4":
                row2 = [char for char in row2]
                row2[2] = first
                row2 = transit.join(row2)
                retired.append(first_move)
                moveset.pop(first_move)
            if first_move == "5":
                row2 = [char for char in row2]
                row2[6] = first
                row2 = transit.join(row2)
                retired.append(first_move)
                moveset.pop(first_move)
            if first_move == "6":
                row2 = [char for char in row2]
                row2[10] = first
                row2 = transit.join(row2)
                retired.append(first_move)
                moveset.pop(first_move)
            if first_move == "7":
                row3 = [char for char in row3]
                row3[2] = first
                row3 = transit.join(row3)
                retired.append(first_move)
                moveset.pop(first_move)
            if first_move == "8":
                row3 = [char for char in row3]
                row3[6] = first
                row3 = transit.join(row3)
                retired.append(first_move)
                moveset.pop(first_move)
            if first_move == "9":
                row3 = [char for char in row3]
                row3[10] = first
                row3 = transit.join(row3)
                retired.append(first_move)
                moveset.pop(first_move)
        
    whitespace()
    
    display_board()
    
    whitespace()
    
    win_condition()

    
def second_move():
    
    whitespace()
    
    global first
    global second
    
    global player_one 
    global player_two
    
    global row1
    global row2
    global row3
    
    global moveset
    
    second_move = None
    retired = []
    
    transit = ''
    
    #ROWS TO LISTS AND BACK TO STRINGS
    
    original_moveset = {"1":row1[2],"2":row1[6],"3":row1[10],"4":row2[2],"5":row2[6],"6":row2[10],"7":row3[2],"8":row3[6],"9":row3[10]}
    
    while second_move not in retired:
        second_move = input(f"Choose where on the board you want to place {second}: ")
        if second_move not in original_moveset:
            print("Sorry, I do not understand what you want to do, please try again.") 
            whitespace()
        if second_move not in moveset and second_move in original_moveset:
            print("Sorry, this position is already taken.")
            whitespace()
        if second_move in moveset:
            if second_move == "1":
                row1 = [char for char in row1]
                row1[2] = second
                row1 = transit.join(row1)
                retired.append(second_move)
                moveset.pop(second_move)
            if second_move == "2":
                row1 = [char for char in row1]
                row1[6] = second
                row1 = transit.join(row1)
                retired.append(second_move)
                moveset.pop(second_move)
            if second_move == "3":
                row1 = [char for char in row1]
                row1[10] = second
                row1 = transit.join(row1)
                retired.append(second_move)
                moveset.pop(second_move)
            if second_move == "4":
                row2 = [char for char in row2]
                row2[2] = second
                row2 = transit.join(row2)
                retired.append(second_move)
                moveset.pop(second_move)
            if second_move == "5":
                row2 = [char for char in row2]
                row2[6] = second
                row2 = transit.join(row2)
                retired.append(second_move)
                moveset.pop(second_move)
            if second_move == "6":
                row2 = [char for char in row2]
                row2[10] = second
                row2 = transit.join(row2)
                retired.append(second_move)
                moveset.pop(second_move)
            if second_move == "7":
                row3 = [char for char in row3]
                row3[2] = second
                row3 = transit.join(row3)
                retired.append(second_move)
                moveset.pop(second_move)
            if second_move == "8":
                row3 = [char for char in row3]
                row3[6] = second
                row3 = transit.join(row3)
                retired.append(second_move)
                moveset.pop(second_move)
            if second_move == "9":
                row3 = [char for char in row3]
                row3[10] = second
                row3 = transit.join(row3)
                retired.append(second_move)
                moveset.pop(second_move)
        
    whitespace()
    
    display_board()
    
    whitespace()

    win_condition()
