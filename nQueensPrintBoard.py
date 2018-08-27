

# Function that prints the board
def printBoard(board):
	N = len(board)
	# For each row print the row with Q as the queen and 0 as nothing
	for i in range(N):
		strToPrint = ["0"]*N
		strToPrint[board[i]] = "Q";
		print(''.join(strToPrint))
