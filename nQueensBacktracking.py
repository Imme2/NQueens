# Implements a backtracking method to solve the NQueens problem
# Guarantees a solution but its much slower.

from collections import defaultdict
from nQueensPrintBoard import printBoard

def NQueensBacktrack(N,board,pos,rowsConflict, conflictsLeft, conflictsRight):
	for i in range(0,N):
		if (rowsConflict[i] == 0 and conflictsRight[pos-i] == 0 and conflictsLeft[pos+i] == 0):
			rowsConflict[i] = 1
			conflictsRight[pos-i] = 1
			conflictsLeft [pos+i] = 1
			board[pos] = i;
			if pos == N - 1:
				return board
			if (NQueensBacktrack(N,board,pos+1,rowsConflict,conflictsLeft,conflictsRight) != False):
				return board
			rowsConflict[i] = 0
			conflictsRight[pos-i] = 0
			conflictsLeft [pos+i] = 0

	return False

def SolveNQueensBacktracking(N):
	if (N <= 3):
		return False

	# Create board
	# Each spot of the array is the column of that row
	# board[0] = 5  -> there's a queen in the position 0,5 
	board = [0 for i in range(N)]

	# Initialize conflict dictionaries
	rowsDict = defaultdict(lambda : 0)
	conflictsLeft = defaultdict(lambda : 0)
	conflictsRight = defaultdict(lambda : 0)

	board = NQueensBacktrack(N,board,0,rowsDict,conflictsLeft,conflictsRight)

	return board



# Gets a number of queens, print solution
if __name__ == "__main__":
	N = int(input())

	board = SolveNQueensBacktracking(N)
	if not board:
		print("We couldn't solve this board")
	else:
		printBoard(board)

