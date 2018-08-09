# Get a number of queens, print solution

from random import shuffle
from collections import defaultdict

if __name__ == "__main__":
	N = int(input())

	board = SolveNQueens(N)

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

	# Helper function because code hell
	getConflicts = lambda x: return rowsDict[board[x]] + conflictsLeft[board[x] + x] + conflictsRight[board[x] - x]

	maxSteps = N + 700 # because why not 

	for steps in range(0,maxSteps):
		# initialize variables
		conflicts = 0
		maxConflicts = 0
		posToChange = 0
		# Choose the position with the most conflicts
		for i in range(0,N):
			conflicts = getConflicts(i)
			posToChange = i if conflicts > maxConflicts else posToChange
			maxConflicts = max(maxConflicts,conflicts)

		# if there are no conflicts we're done
		if maxConflicts == 0:
			break

	return board






