# This code implements the minimum conflict heuristic
# To solve a board, we start from a random state (or a good random state if you have a heuristic)
# Then change the position with the most conflicts to the least conflicts possible.
# Do this iteratively to reach a local optimum (which is hopefully the global one as well)

from random import shuffle
from collections import defaultdict

def printBoard(board):
	N = len(board)
	# For each row print the row with Q as the queen and 0 as nothing
	for i in range(N):
		strToPrint = ["0"]*N
		strToPrint[board[i]] = "Q";
		print(''.join(strToPrint))


def SolveNQueens(N):
	if (N <= 3):
		return False

	# Create board
	# Each spot of the array is the column of that row
	# board[0] = 5  -> there's a queen in the position 0,5 
	board = [i for i in range(N)]

	maxSteps = N**2 + 10000 # because why not 
	maxTries = N + 10

	# try several times as this process depends on how good the initial solution is
	for tries in range(0,maxTries):

		# Initial solution
		# Just place everything randomly (i dont remember a greedy algorithm for this)
		shuffle(board)

		# Build conflict dictionaries
		rowsDict = defaultdict(lambda : 0)
		conflictsLeft = defaultdict(lambda : 0)
		conflictsRight = defaultdict(lambda : 0)

		for i in range(N):
			rowsDict[board[i]] += 1
			left = board[i] + i
			right = board[i] - i
			conflictsLeft[left] += 1
			conflictsRight[right] += 1


		for steps in range(0,maxSteps):
			# initialize variables
			conflicts = 0
			maxConflicts = 0
			posToChange = 0
			# Choose the position with the most conflicts
			for pos in range(0,N):
				conflicts = rowsDict[board[pos]] + conflictsLeft[board[pos] + pos] + conflictsRight[board[pos] - pos]
				posToChange = pos if conflicts > maxConflicts else posToChange
				maxConflicts = max(maxConflicts,conflicts)

			# if there are no conflicts other than the ones caused by itself (3) we're done
			if maxConflicts == 3:
				return board

			if maxConflicts < 3: # if this happens, the code is wrong, there should never be less than 3 conflicts.
				print("Something went wrong")

			# If there were conflicts we gotta try fixing them
			# Choose which new position has the least conflicts
			posMinConflict = board[posToChange]
			minConflict = N**2  # A really big number
			for newPos in range(0,N):
				conflicts = rowsDict[newPos] +  conflictsLeft[newPos + posToChange] + conflictsRight[posToChange - newPos]
				if conflicts < minConflict: # we use lesser than equal in the hopes it'll help with it not getting stuck
					posMinConflict = newPos
					minConflict = conflicts

			# Change that position to the new position

			# Change the conflict dictionaries to identify the change
			rowsDict[board[posToChange]] -= 1
			conflictsLeft[board[posToChange] + posToChange] -= 1
			conflictsRight[board[posToChange] - posToChange] -= 1

			board[posToChange] = posMinConflict

			# Put new conflicts in the dictionaries
			rowsDict[board[posToChange]] += 1
			conflictsLeft[board[posToChange] + posToChange] += 1
			conflictsRight[board[posToChange] - posToChange] += 1

	return False










# Gets a number of queens, print solution
if __name__ == "__main__":
	N = int(input())

	board = SolveNQueens(N)
	if not board:
		print("We couldn't solve this board")
	else:
		printBoard(board)

