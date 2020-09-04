# Sudoku Solver

class Square: # define 'square' object with parameters row, col and value
	def __init__( self, row, col, value):
		self.row = row
		self.col = col
		self.value = value
		

def fill(board): # board is a 2d array
	curr_square = find_empty_square(board) # find an empty square
	if curr_square.value: # if curr_square value is not 0, i.e. not empty
		return True
	for i in range(1,10): # try each value that is valid
		if is_valid(board,curr_square,i): # if value works, go deeper
			board[curr_square.row][curr_square.col] = i
			print("BOARD:")
			for i in range(0,len(board)): # print board!!
				print (board[i])
			if fill(board):
				return True
		board[curr_square.row][curr_square.col] = 0 # if it recurses back, try new value
	return False; # unsolvable board
	
	
def find_empty_square(board):
	for i in range(0,len(board)):
		for j in range(0,len(board[i])):
			if board[i][j] == 0: # if it equals 0, i.e. is empty
				square = Square(i,j,0)
				return square
	square = Square(i,j,10)	 # no empty squares
	return square

def is_valid(board,square,int):
	if int < 1 or int > 9:
		return False
		
	for i in range(0,len(board[0])): # check row
		if board[square.row][i] == int:
			return False
		
	for i in range(0,len(board)): # check column
		if board[i][square.col] == int:
			return False
			
	# CHECK BOX!!!
	start_row = square.row - (square.row % 3)
	start_col = square.col - (square.col % 3)
	# iterate over the 3 by 3 box
	for i in range(0,3):
		for j in range(0,3):
			if board[start_row+i][start_col + j] == int:
				return False
	
	return True;

board = [[4,0,0,0,0,0,0,0,0],[0,0,0,0,0,9,0,0,0],[0,0,0,0,0,0,7,8,5],[0,0,7,0,4,8,0,5,0],[0,0,1,3,0,0,0,0,0],[0,0,6,0,7,0,0,0,0],[8,6,0,0,0,0,9,0,3],[7,0,0,0,0,5,0,6,2],[0,0,3,7,0,0,0,0,0]]
# THIS BOARD WORKS: board = [[0,0,0,0,0,5,0,0,0],[4,0,0,2,0,0,0,1,0],[0,6,1,0,0,0,0,0,0],[0,0,7,0,2,6,0,0,0],[0,0,9,5,0,0,0,0,7],[0,0,0,0,0,0,3,0,0],[0,0,8,6,0,0,0,0,0],[0,4,0,0,0,7,0,0,3],[0,5,0,1,0,9,7,2,0]]
# THIS BOARD WORKS: board = [[0,8,0,0,0,0,2,0,0],[0,0,0,0,8,4,0,9,0],[0,0,6,3,2,0,0,1,0],[0,9,7,0,0,0,0,8,0],[8,0,0,9,0,3,0,0,2],[0,1,0,0,0,0,9,5,0],[0,7,0,0,4,5,8,0,0],[0,3,0,7,1,0,0,0,0],[0,0,8,0,0,0,0,4,0]]
fill(board)
for i in range(0,len(board)): # print board!!
	print (board[i])