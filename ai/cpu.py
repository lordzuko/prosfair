import imp
import json
import copy
<<<<<<< HEAD
#chessboard = json.load(open("../common/initial_state.json"))
rules = imp.load_source('chess_basic_rules','../common/rules.py')
piece_value = json.load(open("../common/chess_piece_priority.json"))

opposite = { "white" : "black" , "black" : "white" }

def generate_board(board,move):
	new_board = copy.deepcopy(board)
	killed_piece = None
	for k,v in new_board[opposite[move['color']]].iteritems(): 
		if move['new_position'] == v :
			killed_piece = k

	if killed_piece and killed_piece in new_board[opposite[move['color']]].keys() : del new_board[opposite[move['color']]][killed_piece]

	#if killed_piece :	print killed_piece

	new_board[move['color']][move['piece']] = move['new_position']
	return new_board
=======

rules = imp.load_source('chess_basic_rules','../common/rules.py')
piece_value = json.load(open("../common/chess_piece_priority.json"))
helper = imp.load_source('helper_functions','../common/helper_functions.py')

opposite = { "white" : "black" , "black" : "white" }


def emperical_comparision(board,color):
	return sum([ float(piece_value[x]) for x in board[color].keys() ]) - \
		sum( [ float(piece_value[x]) for x in board[opposite[color]].keys() ])
>>>>>>> b8a2f02eb9771dd5b66fcae0fe53a382db103934

def risk_comparision(board,color):
	return sum([ float(piece_value[x]) for x in board[opposite[color]].keys() if helper.if_piece_under_attack(board,opposite[color],x) ]) - \
		sum([ float(piece_value[x]) for x in board[color].keys() if helper.if_piece_under_attack(board,color,x) ] ) 		

def defence_comparision(board,color):
	return sum([ float(helper.shielding(board,color,x)) for x in board[color].keys() ]) - \
		sum ([ float(helper.shielding(board,opposite[color],x))  for x in board[opposite[color]].keys() ] )



def evaluate_board(board,color):
	if helper.in_checkmate(board,color) or helper.in_check(board,color):	return float('-inf')
	if helper.in_checkmate(board,opposite[color]) or helper.in_check(board,opposite[color]): return float('inf')
 	##TODO: here only two extremes cases has only been handled
	##      need to write the middle cases, which will include
	## 	the current position of the player's pieces.

<<<<<<< HEAD
def in_check(board,color):
	oc = opposite[color]
	moves = []
	for x in board[oc].keys():
		if   "king"   in x:
			moves = moves +  rules.legal_king_moves(board,oc,x)
		elif "queen"  in x:
			moves = moves +  rules.legal_queen_moves(board,oc,x)
		elif "bishop" in x:
			moves = moves +  rules.legal_bishop_moves(board,oc,x)
		elif "knight" in x: 
			moves = moves +  rules.legal_knight_moves(board,oc,x)
		elif "rook"   in x:
			moves = moves +  rules.legal_rook_moves(board,oc,x)
		elif "pawn"   in x:
			moves = moves +  rules.legal_pawn_moves(board,oc,x)
	if 'king' in board[color].keys():
		if board[color]['king'] in moves:
			return True
=======
	emperical_eval = emperical_comparision(board,color)	
	risk_eval      = risk_comparision(board,color)
	defence_eval   = defence_comparision(board,color)
	
	print emperical_eval , risk_eval  , defence_eval 
	
	return risk_eval

>>>>>>> b8a2f02eb9771dd5b66fcae0fe53a382db103934


<<<<<<< HEAD
def game_over(board,color):
	if in_checkmate(board,color) or in_checkmate(board,opposite[color]) :	return True
	return False

def evaluate_board(board,color):
	if in_checkmate(board,color) or in_check(board,color):	return -1.0
	if in_checkmate(board,opposite[color]) or in_check(board,opposite[color]): return 1.0
 	##TODO: here only two extremes cases has only been handled
	##      need to write the middle cases, which will include
	## 	the current position of the player's pieces.

	return sum([ float(piece_value[x]) for x in board[color].keys() ]) - sum( [ float(piece_value[x]) for x in board[opposite[color]].keys() ])

 
	



def get_moves(board,color):
	moves_list  = []
	moves = []

	for x in board[color].keys():
		if   "king"   in x:
			moves = rules.legal_king_moves(board,color,x)
		elif "queen"  in x:
			moves = rules.legal_queen_moves(board,color,x)
		elif "bishop" in x:
			moves = rules.legal_bishop_moves(board,color,x)
		elif "knight" in x:
			moves = rules.legal_knight_moves(board,color,x)
		elif "rook"   in x:
			moves = rules.legal_rook_moves(board,color,x)
		elif "pawn"   in x:
			moves = rules.legal_pawn_moves(board,color,x)
		
		for move in moves:
			moves_list = moves_list + [ {"color": color,"piece":x,"new_position":move}  ]
	
	return moves_list
=======

>>>>>>> b8a2f02eb9771dd5b66fcae0fe53a382db103934

def minimax(board,color,depth):

	if depth == 0 : return evaluate_board(board,color)
	
	moves_list = helper.get_moves(board,color)

	if len(moves_list) == 0: return None

	best_move = moves_list[0]
	best_score = float('-inf')

	for move in moves_list:
<<<<<<< HEAD
		clone_board = generate_board(board,move)
=======
		clone_board = helper.generate_board(board,move)
>>>>>>> b8a2f02eb9771dd5b66fcae0fe53a382db103934
		score = min_play(clone_board,opposite[color],depth)
		if score > best_score:
			best_move= move
			best_score = score
	
	return best_move
	

def min_play(board,color,depth):
	if helper.game_over(board,color) or depth <= 0:
		return evaluate_board(board,color)

	moves_list = helper.get_moves(board,color)
	best_score = float('inf')
	
	for move in moves_list:
<<<<<<< HEAD
		clone_board = generate_board(board,move)
		score  =max_play(clone_board,opposite[color],depth-1)
		#rint "evaluating move : ", move, score
=======
		clone_board = helper.generate_board(board,move)
		score  =max_play(clone_board,opposite[color],depth-1)
		#print "evaluating move : ", move, score
>>>>>>> b8a2f02eb9771dd5b66fcae0fe53a382db103934
		if score < best_score:
			best_move = move
			best_score = score

	return best_score



def max_play(board,color,depth):
	if helper.game_over(board,color) or depth <= 0 :
		return evaluate_board(board,color)

	moves_list = helper.get_moves(board,color)

	best_score = float('-inf')

	for move in moves_list:
		clone_board = helper.generate_board(board,move)
		score = min_play(clone_board,color,depth-1)
<<<<<<< HEAD
		#rint "evaluating move : ", move,score
=======
		#print "evaluating move : ", move,score
>>>>>>> b8a2f02eb9771dd5b66fcae0fe53a382db103934

		if score > best_score:
			best_move = move
			best_score = score
	
	return best_score




<<<<<<< HEAD
#print minimax(chessboard,"white",3)
=======
>>>>>>> b8a2f02eb9771dd5b66fcae0fe53a382db103934
