import math
from state_space import *

										   #depth taken as input
def alpha_beta(board, turn, player, child, depth): 

	moves = actions(board, child) #generate actions for current board state

	best_util = -math.inf #util
	flag_index = 0		  #if best_util has been changed
	action_index = -1

	alpha = -math.inf	  
	beta = math.inf



	for move in moves:
		(k, i, j) = move

							#    board                      turn            player   alphabeta     depth      
		temp_util = min_value(result(board, move, turn), toggle_turn(turn), player, (alpha, beta), move, depth-1)


		if (temp_util > best_util):
			best_util = temp_util
			action_index = flag_index  # if changed save best action's index

		# undo result() and toggle_turn() 
		
		board[k][i][j] = '.'
		# print(board)


		alpha = max(alpha, best_util)


		flag_index = flag_index + 1


	return moves[action_index]






def max_value(board, turn, player, alphabeta, child, depth):
	alpha = alphabeta[0]
	beta = alphabeta[1]

	status = terminal_test(board, child)   #'d'/'o'/'x'/'n' for previous action

	if (status != 'n'):               #if terminated 
		return utility(status, player)

	else:
		if (depth == 0):
			return eval(board, player)


		else:     #if not terminated

			moves = actions(board, child) #generate actions for current board state
			best_util = -math.inf   

			for move in moves:
				(k,i,j) = move

														# board 					turn 		   player 	alphabeta 	  child  depth
				best_util = max(best_util, min_value(result(board, move, turn), toggle_turn(turn), player, (alpha, beta), move, depth-1))


				# undo result() and toggle_turn() 
				
				board[k][i][j] = '.'




				if (best_util >= beta):
					return best_util

				else:
					alpha = max(alpha, best_util)

			return best_util



def min_value(board, turn, player, alphabeta, child, depth):

	alpha = alphabeta[0]
	beta = alphabeta[1]


	status = terminal_test(board, child)   #'d'/'o'/'x'/'n'


	if (status != 'n'):
		return utility(status, player)


	else:
		if (depth == 0):
			return eval(board, player)

		else: 

			moves = actions(board, child) #generate actions for current board state
			worst_util = math.inf

			for move in moves:
				(k,i,j) = move

				worst_util = min(worst_util, max_value(result(board, move, turn), toggle_turn(turn) , player, (alpha, beta), move, depth-1))

				# undo result() and toggle_turn() 
				
				board[k][i][j] = '.'


				if (worst_util <= alpha):
					return worst_util

				else:
					beta = min(beta, worst_util)

			return worst_util


# assuming player is 'x'

	# x . .  +10
	# x x .  +70
	# x x x  +100
	# o . .  -10
	# o o .  -70
	# o o o  -100
	# rest   0



def eval(board, player):
	player_score = 0
	# print(board)


	for child in board: # k
		if (not full_board(child)):     #full board skipped with value 0

			for row in child:
				eval_support(player_score, row, player)



			for column in range(0,3):
				eval_support(player_score, [child[0][column], child[1][column], child[2][column]] , player)

			#diagnal
			eval_support(player_score, [child[0][0], child[1][1], child[2][2]] , player)
			eval_support(player_score, [child[0][2], child[1][1], child[2][0]] , player)

	return player_score



def eval_support(player_score, line, player):

	player_count = np.count_nonzero(line == player)
	opponent_count = np.count_nonzero(line == toggle_turn(player))
	dot_count = np.count_nonzero(line == '.')


	if (player_count == 1 and dot_count == 2):
		player_score = player_score + 10

	elif (player_count == 2 and dot_count == 1):
		player_score = player_score + 70

	elif (opponent_count == 1 and dot_count == 2):
		player_score = player_score - 10

	elif (opponent_count == 2 and dot_count == 1):
		player_score = player_score - 70







		

		


def full_board(board):      # for testing 'n'

	for i in range(0,3):
		for j in range(0,3):
			if (board[i][j] == '.'):
				return False

	return True






def utility(status, player):

	if (status == 'd'):
		return 0

	elif (status == 'o'):       
		
		if (player == 'o'):
			return 100
		else:
			return -100


	elif (status == 'x'):

		if (player == 'o'):
			return -100

		else:
			return 100	









