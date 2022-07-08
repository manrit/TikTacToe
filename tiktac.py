import random 
def display_board(board):
    
    print()
    print(board[1]+"  |  "+board[2]+"  |  "+board[3] )
    print("_______________")
    print()
    print(board[4]+"  |  "+board[5]+"  |  "+board[6])

    print("_______________")
    print()
    print(board[7]+"  |  "+board[8]+"  |  "+board[9])
    

def player_input():
  marker = ''
  while not (marker == 'X' or marker == 'O'):

     marker = input("player 1, pick a marker 'X' or 'O': ").upper()

  if marker == "X":
    return('X', 'O')
  else: 
    return('O', 'X')


def place_marker(board, marker, position):
  
  board[position] = marker

def win_check(board, mark):
   
    return (board[4]==board[5]==board[6]== mark) or (board[1]==board[2]==board[3]== mark) or (board[7]==board[8]==board[9]== mark) or (board[1]==board[4]==board[7]== mark) or (board[2]==board[5]==board[8]== mark) or (board[3]==board[6]==board[9]== mark) or (board[1]==board[5]==board[9]== mark) or (board[3]==board[5]==board[7]== mark)

def choose_first():
  flip = random.randint(0,1)
  if flip == 0:
    return 'player 1'
  else:
    return 'Player 2'

def space_check(board, position):

 return board[position] == ' ' 

def full_board_check(board):
  for i in range(1, 10):
    if space_check(board, i):
      return False
  #board full if return True
  return True

def player_choice(board):
  position = 0

  while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
    position = int(input('Choose a position 1-9: '))
  return position

def replay():
  choice = input("play again? Y or N: ")
  return choice == "Y"

print('Welcome to Tic Tac Toe')

#set up board,markers, who's first,\ 
while True:

  the_board = [' ']*10
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(turn + " will go first!")

  play_game = input('Ready to play? Y or N? ').upper()
  if play_game == 'Y':
    game_on = True
  else:
    game_on = False
  
  #game
  while game_on:
    if turn == 'player 1':
      #show board
      display_board(the_board)
      #choose position
      position = player_choice(the_board)
      #Place marker at positon
      place_marker(the_board, player1_marker, position)

      #did they win?
      if win_check(the_board, player1_marker ):
        display_board(the_board)
        print('Player 1 has WON!!')
        game_on = False

      #or is there a tie?
      else:
        if full_board_check(the_board):
          display_board()
          print('The games a TIE!')
          game_on = False
        else:
          turn = 'player 2'
      #no tie or no win -> next player turn

    else:
       #show board
      display_board(the_board)
      #choose position
      position = player_choice(the_board)
      #Place marker at positon
      place_marker(the_board, player2_marker, position)

      #did they win?
      if win_check(the_board, player2_marker ):
        display_board(the_board)
        print('Player 2 has WON!!')
        game_on = False

      #or is there a tie?
      else:
        if full_board_check(the_board):
          display_board()
          print('The games a TIE!')
          game_on = False
        else:
          turn = 'player 1'
     
  if not replay():
    break


