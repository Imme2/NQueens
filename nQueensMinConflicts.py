# This code implements the minimum conflict heuristic
# To solve a board, we start from a random state (or a good random state if you have a heuristic)
# Then change the position with the most conflicts to the least conflicts possible.
# Do this iteratively to reach a local optimum (which is hopefully the global one as well)



from random import shuffle
from collections import defaultdict

# Gets a number of queens, print solution
if __name__ == "__main__":
	N = int(input())

	board = SolveNQueens(N)
	if not board:
		print("We couldn't solve this board")
	else:
		printBoard(board)

def printBoard(board):
	N = len(board)
	# For each row print the row with Q as the queen and 0 as nothing
	for i in range(N):
		strToPrint = "0"*N
		strToPrint[board[i]] = "Q";
		print(strToPrint)


def SolveNQueens(N):
	if (N <= 3):
		return False

	# Create board
	# Each spot of the array is the column of that row
	# board[0] = 5  -> there's a queen in the position 0,5 
	board = [i for i in range(N)]

	# Initial solution
	# Just place everything randomly (i dont remember a greedy algorithm for this)
	shuffle(board)

	# Build conflict dictionaries
	rowsDict = defaultdict(lambda x: 0)
	conflictsLeft = defaultdict(lambda x: 0)
	conflictsRight = defaultdict(lambda x: 0)

	for i in range(N):
		rowsDict[board[i]] += 1
		left = board[i] + i
		right = board[i] - i
		conflictsLeft[left] += 1
		conflictsRight[right] += 1

	# Helper function because otherwise it'll get too long
	# For python newbies this is just a function declaration, where x is an argument and
	# the return is the body of it.
	getConflicts = lambda x: return rowsDict[board[x]] + conflictsLeft[board[x] + x] + conflictsRight[board[x] - x]

	maxSteps = N + 700 # because why not 

	for steps in range(0,maxSteps):
		# initialize variables
		conflicts = 0
		maxConflicts = 0
		posToChange = 0
		# Choose the position with the most conflicts
		for pos in range(0,N):
			conflicts = getConflicts(pos)
			posToChange = pos if conflicts > maxConflicts else posToChange
			maxConflicts = max(maxConflicts,conflicts)

		# if there are no conflicts we're done
		if maxConflicts == 0:
			return board

		# If there were conflicts we gotta try fixing them
		# Choose which new position has the least conflicts
		posMinConflict = board[posToChange]
		minConflict = N**2  # A really big number
		for newPos in range(0,N):
			conflicts = rowsDict[newPos] +  conflictsLeft[newPos + posToChange] + conflictsRight[posToChange - newPos]
			if conflicts <= minConflict: # we use lesser than equal in the hopes it'll help with it not getting stuck
				posMinConflict = newPos
				minConflict = conflicts

		# Change that position to the new position
		board[posToChange] = posMinConflict

	return False






