import math
import sys
from state_space import *
from HMinimax import *


#input in form of ex) 34   (3rd board 4th location)



def run():
	# print("please choose the algorithm to play against")
	# mode = input("a: minimax,  b: h-minimax")
	# if (mode == "a"):


	player = input("please choose o or x: ")


	print("x goes first")

	board, turn, player, child = initialize(player)



	if (player == 'x'):
		#player = 'x'   computer = 'o'
		# player -> computer loop   while game is not over
		while (terminal_test(board, child) == 'n'):

			print_board(board)


			if (child == (-1,-1,-1) or full_board(board[translate_output(child)])):    #can place anywhere  for starting turn or draw from previous action
				x_move = input("please place a move anywhere: ")   #ex) 34
				(temp_i, temp_j) = translate_input(x_move[1])
				x_move = (int(x_move[0]) - 1, temp_i, temp_j)

				while(not valid_move(board, x_move)):
					x_move = input("please place a valid move anywhere: ")
					(temp_i, temp_j) = translate_input(x_move[1])
					x_move = (int(x_move[0]) - 1, temp_i, temp_j)





			else: #specify the board for them referencing 'child' move
				target = translate_output(child)
				temp_move = translate_input(input("please place a move on board number " + str(target + 1) + ": "))   #ex) 3
				x_move = (target, temp_move[0], temp_move[1])

				while(not valid_move(board, x_move)):
					temp_move = translate_input(input("please place a valid move on board number " + str(target + 1) + ": "))
					x_move = (target, temp_move[0], temp_move[1])

			# print(x_move)


			board, turn, child = transition_model(board, x_move, 'x')  #player move



			if (terminal_test(board, child) != 'n'):
				break;


			#computer turn
			print_board(board)


			o_move = alpha_beta(board, 'o', 'o', child, 10)   #minimax to computer's favor

			board, turn, child = transition_model(board, o_move, 'o')





	else:
		#player = 'o'   computer = 'x'
		# computer -> player loop   while game is not over
		while (terminal_test(board, child) == 'n'):

			#computer turn

			print_board(board)

			x_move = alpha_beta(board, 'x', 'x', child, 10)  #minimax to computer's favor

			# print(board)
			# print(x_move)
			

			board, turn, child = transition_model(board, x_move, 'x')


			if (terminal_test(board, child) != 'n'):
				break;

			#player turn

			print_board(board)
			# print(board)



			if (child == (-1,-1,-1) or full_board(board[translate_output(child)])):    #can place anywhere  for starting turn or draw from previous action
				o_move = input("please place a move anywhere: ")   #ex) 34

				while(not valid_move(board, o_move)):
					o_move = input("please place a valid move anywhere: ")

				(temp_i, temp_j) = translate_input(o_move[1])
				o_move = (int(o_move[0]) - 1, temp_i, temp_j)



			else: #specify the board for them referencing 'child' move
				target = translate_output(child)
				temp_move = translate_input(input("please place a move on board number " + str(target + 1) + ": "))   #ex) 3
				o_move = (target, temp_move[0], temp_move[1])

				while(not valid_move(board, o_move)):
					temp_move = translate_input(input("please place a valid move on board number " + str(target + 1) + ": "))
					o_move = (target, temp_move[0], temp_move[1])



			board, turn, child = transition_model(board, o_move, 'o')  #player move



	winner = terminal_test(board, child)
	print_board(board)
	if (winner == 'd'):
		print("it is a draw!")
	else:
		print("Winner is: " + winner)





# 1 2 3
# 4 5 6
# 7 8 9


					





if __name__ == "__main__":
	run()

















