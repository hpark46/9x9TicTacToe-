import random
import numpy as np

#state
def initialize(playtype):   #input x or o
	
	board = []       #9x9 board (main board)
	cell = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]      #[k][i][j]
	for num in range(0,9):
		board.append(cell)

	board = np.array(board)


	turn = 'x'
	player = playtype

	return board, turn, player, (-1,-1,-1)      # 9 x 3x3 , x/o , x/o, initial previous action



#action (possible actions inside specific child board or any board (if child board is terminated (draw)))

def actions(board, child):     # board, previous action performed (k,i,j)

	target = -1                # target board for next move
	(child_k, child_i, child_j) = child

	if (child == (-1,-1,-1)):
		target = random.randint(0,8)  #b/c I do not have positional evaluation, used random

	else:
		target = translate_output(child)


	moves = []

	for i in range(0,3):
		for j in range(0,3):
			if (board[target][i][j] == '.'):
				moves.append((target,i,j))      # (k,i,j)


	#check if there are no possible moves at the target (draw), if there are no moves, player can place anywhere
	if (len(moves) == 0):
		for k in range(0,9):
			for i in range(0,3):
				for j in range(0,3):
					moves.append( (k,i,j) )


	return moves



def transition_model(board, action, turn):

	#      updated board 				toggled turn       performed action
	# print(result(board, action,))
	return result(board, action, turn), toggle_turn(turn), action    




def result(board, action, turn):

	(k,i,j) = action
	# print((k,i,j))
	# print_board(board)
	# print("*******")

	board[k][i][j] = turn
	# print(board)
	# print_board(board)
	# print("+++++++++")

	return board


def toggle_turn(turn):

	if (turn == 'x'):
		return 'o'

	else:
		return 'x'




def terminal_test(main_board, previous_action):
	if (previous_action == (-1,-1,-1)):
		return 'n'

	else:

		(k,i,j) = previous_action
		board = main_board[k]

		for row in board:
			if (row[0] == row[1] == row[2] != '.'):
				# print(111111)
				return row[0]   #terminated with winner


		for column in range(0, 3):
			if (board[0][column] == board[1][column] == board[2][column] != '.'):
				# print(22222)
				return board[0][column]   #terminated with winner


		if (board[0][0] == board[1][1] == board[2][2] != '.' or board[0][2] == board[1][1] == board[2][0] != '.'):
			# print(33333)
			return board[1][1]    #terminated with winner


		else:
			flag = True

			for i in range(0,3):
				for j in range(0,3):
					if (board[i][j] == '.'):
						flag = False

			if (flag == True):
				# print(444444)
				return 'd'       #if full board draw

			else:
				# print(55555)
				return 'n'       #if not full board (game not over)





def translate_output(input_action):      
	(input_k, input_i, input_j) = input_action
	action = (input_i, input_j)


	if (action == (-1,-1)):
		return -1
	elif (action == (0,0)):
		return 0
	elif (action == (0,1)):
		return 1
	elif (action == (0,2)):
		return 2
	elif (action == (1,0)):
		return 3
	elif (action == (1,1)):
		return 4
	elif (action == (1,2)):
		return 5
	elif (action == (2,0)):
		return 6
	elif (action == (2,1)):
		return 7
	else:
		return 8						






def print_board(board):
	hold = ""
	for i in range(0,3):
		for k in range(0,3):
			hold = hold + board[k][i][0] + " " + board[k][i][1] + " " + board[k][i][2] + "|"
		print(hold)
		hold = ""

	print("")

	for i in range(0,3):
		for k in range(3,6):
			hold = hold + board[k][i][0] + " " + board[k][i][1] + " " + board[k][i][2] + "|"
		print(hold)
		hold = ""

	print("")

	for i in range(0,3):
		for k in range(6,9):
			hold = hold + board[k][i][0] + " " + board[k][i][1] + " " + board[k][i][2] + "|"
		print(hold)
		hold = ""

	print("")



def translate_input(cell_number):      

	if (cell_number == '1'):
		return (0,0)
	elif (cell_number == '2'):
		return (0,1)
	elif (cell_number == '3'):
		return (0,2)
	elif (cell_number == '4'):
		return (1,0)
	elif (cell_number == '5'):
		return (1,1)
	elif (cell_number == '6'):
		return (1,2)
	elif (cell_number == '7'):
		return (2,0)
	elif (cell_number == '8'):
		return (2,1)
	else:
		return (2,2)	




def valid_move(board, move): # checking input of 'human player'

	(k,i,j) = move
	if (board[k][i][j] != '.'):
		return False

	else:
		return True



