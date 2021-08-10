def player_input():
    marker=''
    
    while marker!='X' and marker!='O':
        marker=input('Player 1, choose X or O: ').upper()
    
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    
    return(player1,player2)

#j'importe la fonction native clear_output pour obtenir seulement la dernière version de ma table de jeu
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

#la fonction place le marqueur à une position donnée sur la table de jeu
def place_marker(board,marker,position):
    board[position]=marker

def check_winner(board,marker):
    #un gagnant ?
    return(
    #combinaison gagnante dans une ligne ?
    (board[7]==board[8]==board[9]==marker) or
    (board[4]==board[5]==board[6]==marker) or
    (board[1]==board[2]==board[3]==marker) or    
    #combinaison gagnante dans une colonne ?
    (board[7]==board[4]==board[1]==marker) or
    (board[8]==board[5]==board[2]==marker) or
    (board[9]==board[6]==board[3]==marker) or
    #combinaison gagnante en diagonale ?
    (board[7]==board[5]==board[3]==marker) or
    (board[1]==board[5]==board[9]==marker))

#choisir le premier joueur
import random
def choose_first_player():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'

#je vérifie que l'action est possible et que la place n'est pas déjà occupée
def isValidAction(board,position):
    return board[position]=='-'

def full_board():
    for i in range(1,10):
        if isValidAction(board,i):
            #si l'action est valide alors la table n'est pas pleine donc on retourne false
            return False
    return True

def player_choice(board):
    position=0
    while position not in range(1,10) or not isValidAction(board,position):
        position=int(input('Choose a position (1-9): '))
    return position

def start_new_game():
    choice='Choose'
    while choice!='Yes' and choice!='No':
        choice=input('Do you want to play again? Enter Yes or No: ').capitalize()
    return choice=='Yes'

#Boucle qui permet de faire tourner le jeu
print('TIC TAC TOE')
while True:
    #Play
    board=['-']*10
    player1_marker,player2_marker=player_input()
    
    turn=choose_first_player()
    print(turn+' GO FIRST!')
    
    play_game='ready'
    while play_game!='Yes' and play_game!='No':
        play_game=input('Ready to play? Yes or No: ').capitalize()
        if play_game=='Yes':
            game_on=True
        else:
            game_on=False
    
    while game_on:
        #Tour du 1er joueur
        if turn=='Player 1':
            display_board(board)
            #Choix position
            position=player_choice(board)
            #placement du marqueur
            place_marker(board,player1_marker,position)
            #winner?
            if check_winner(board,player1_marker):
                display_board(board)
                print('PLAYER 1 WON!')
                game_on=False
            #tie?
            else:
                if full_board():
                    display_board(board)
                    print('WE HAVE A TIE!')
                    game_on=False
                #next player
                else:
                    turn='Player 2'
           
        else:
            #Tour du 2ème joueur
            display_board(board)
            #Choix position
            position=player_choice(board)
            #placement du marqueur
            place_marker(board,player2_marker,position)
            #winner?
            if check_winner(board,player2_marker):
                display_board(board)
                print('PLAYER 2 WON!')
                game_on=False
            #tie?
            else:
                if full_board():
                    display_board(board)
                    print('WE HAVE A TIE!')
                    game_on=False
                #next player
                else:
                    turn='Player 1'
                    
    #Break dans la boucle ('Do you want to play again ? 'No')
    if not start_new_game():
        break