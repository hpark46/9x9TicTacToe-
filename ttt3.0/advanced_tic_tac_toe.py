import math
import sys
from state_space import *
from Minimax import *



def run():
	# print("please choose the algorithm to play against")
	# mode = input("a: minimax,  b: h-minimax")
	# if (mode == "a"):


	player = input("please choose o or x: ")


	print("x goes first")

	board, turn, player = initialize(player)



	if (player == 'x'):
		#player = 'x'   computer = 'o'
		# player -> computer loop   while game is not over
		while (terminal_test(board) == 'n'):

			print_board(board)
			print('')

			x_move = translate_input(input("please place a move: "))


			while (not valid_move(board, x_move)):
				x_move = translate_input(input("please place a valid move: "))


			board, turn = transition_model(board, x_move, 'x')  #player move



			if (terminal_test(board) != 'n'):
				break;


			#computer turn
			print_board(board)
			print('')


			o_move = minimax(board, 'o', 'o')   #minimax to computer's favor

			board, turn = transition_model(board, o_move, 'o')





	else:
		#player = 'o'   computer = 'x'
		# computer -> player loop   while game is not over
		while (terminal_test(board) == 'n'):

			#computer turn

			print_board(board)
			print('')

			x_move = minimax(board, 'x', 'x')  #minimax to computer's favor


			board, turn = transition_model(board, x_move, 'x')


			if (terminal_test(board) != 'n'):
				break;

			#player turn

			print_board(board)
			print('')

			o_move = input("please place a move: ")
			o_move = translate_input(o_move)

			while (not valid_move(board, o_move)):
				o_move = translate_input(input("please place a valid move: "))


			board, turn = transition_model(board, o_move, 'o')  #player move


	winner = terminal_test(board)
	if (winner == 'd'):
		print("it is a draw!")
	else:
		print("Winner is: " + winner)





# 1 2 3
# 4 5 6
# 7 8 9


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





if __name__ == "__main__":
	run()

















