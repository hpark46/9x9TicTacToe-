#state
def initialize(playtype):   #input x or o
	
	board = []
	cell = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
	for num in range(0,9):
		board.append(cell)


	turn = 'x'
	player = playtype

	return board, turn, player



#action
def actions(board):
	moves = []
	for i in range(0,3):
		for j in range(0,3):
			if (board[i][j] == '.'):
				# actions.append(i*3 + j)
				moves.append((i,j))

	return moves



#transition_model
def transition_model(board, action, turn):

	return result(board, action, turn), toggle_turn(turn)




def result(board, action, turn):

	(i,j) = action
	board[i][j] = turn

	return board



def toggle_turn(turn):
	
	if (turn == 'x'):
		return 'o'

	else:
		return 'x'



#terminal state


def terminal_test(board): # 'd': draw  'o'/'x': winner  'n': not terminated

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











def print_board(board):
	hold = ""
	for rows in board:
		hold = rows[0]+" "+rows[1]+ " "+ rows[2]
		print(hold)




def valid_move(board, move):
	(i,j) = move
	if (board[i][j] == '.'):
		return True

	else:
		return False




