#state
def initialize(playtype):   #input x or o
	
	board = []       #9x9 board (main board)
	cell = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]     #child board 
	for num in range(0,9):
		board.append(cell)


	turn = 'x'
	player = playtype

	return board, turn, player      # 9 x 3x3 , x/o , x/o



#action (possible actions inside specific child board)

def actions(board, child):     # board, previous action performed (i,j)

	target = board[translate_output(child)]   #specific board for next move

	moves = []
	for i in range(0,3):
		for j in range(0,3):
			if (target[i][j] == '.'):

				moves.append((i,j))

	return moves



#transition_model		child (previous action) given as (i,j)

def transition_model(board, action, turn, child):

	return result(board, action, turn, child), toggle_turn(turn)



# action returned for determining next target child board 
def result(board, action, turn, child): 

	target = board[translate_output(child)]
	(i,j) = action

	target[i][j] = turn

	return board, action #child



def toggle_turn(turn):
	
	if (turn == 'x'):
		return 'o'

	else:
		return 'x'



#terminal state

# terminal test on the child board of last placed action
def terminal_test(main_board, previous_action): # 'd': draw  'o'/'x': winner  'n': not terminated

	board = main_board[translate_output(previous_action)]


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





def translate_output(action):      

	if (action == (0,0)):
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
	for rows in board:
		hold = rows[0]+" "+rows[1]+ " "+ rows[2]
		print(hold)




def valid_move(board, move, child):

	target = board[translate_output(child)]

	(i,j) = move
	if (target[i][j] == '.'):
		return True

	else:
		return False




