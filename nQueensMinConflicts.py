# This code implements the minimum conflict heuristic
# To solve a board, we start from a random state (or a good random state if you have a heuristic)
# Then change the position of a threatened queen to the least conflicts possible.
# Do this iteratively to reach a local optimum (which is hopefully the global one as well)

from random import shuffle,choice
from collections import defaultdict
from nQueensPrintBoard import printBoard

def SolveNQueensMinConflict(N):
	if (N <= 3):
		return False

	# Create board
	# Each spot of the array is the column of that row
	# board[0] = 5  -> there's a queen in the position 0,5 
	board = [i for i in range(N)]

	maxSteps = N + 1000  # it usually solves in less than 200 when it does. 
						 # So a low number of steps actually makes it more efficient
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

		changes = 0
		for steps in range(0,maxSteps):
			# initialize variables
			threatened = []
			conflicts = 0
			maxConflicts = 0
			posToChange = 0
			# check conflicts and collect the threatened positions
			for pos in range(0,N):
				conflicts = rowsDict[board[pos]] + conflictsLeft[board[pos] + pos] + conflictsRight[board[pos] - pos]
				if conflicts > 3:
					threatened += [pos]

			# If none are threatened, we're done
			if len(threatened) == 0:
				#print("Done, changes done",changes)
				return board
			
			# If there's threatened queens, choose randomly from them
			posToChange = choice(threatened)

			# If there were conflicts we gotta try fixing them
			# Choose which new position has the least conflicts
			posMinConflict = board[posToChange]

			# minConflict is the current one
			minConflict = (rowsDict[board[posToChange]] != 0) +  (conflictsLeft[board[posToChange] + posToChange] != 0) + (conflictsRight[board[posToChange] - posToChange] != 0)
			for newPos in range(0,N):
				conflicts = (rowsDict[newPos] != 0) +  (conflictsLeft[newPos + posToChange] != 0) + (conflictsRight[newPos - posToChange] != 0)
				if conflicts < minConflict: # we use lesser than equal in the hopes it'll help with it not getting stuck
					posMinConflict = newPos
					minConflict = conflicts

			# Change that position to the new position

			# Change the conflict dictionaries to identify the change

			# Dont do unnecesary changes:
			if (board[posToChange] != posMinConflict):				
				rowsDict[board[posToChange]] -= 1
				conflictsLeft[board[posToChange] + posToChange] -= 1
				conflictsRight[board[posToChange] - posToChange] -= 1

				changes += 1


				board[posToChange] = posMinConflict

				# Put new conflicts in the dictionaries
				rowsDict[board[posToChange]] += 1
				conflictsLeft[board[posToChange] + posToChange] += 1
				conflictsRight[board[posToChange] - posToChange] += 1

		#print("new try #",tries,":\n Changes done: ",changes)

	return False


# Gets a number of queens, print solution
if __name__ == "__main__":
	N = int(input())

	board = SolveNQueensMinConflict(N)
	if not board:
		print("We couldn't solve this board")
	else:
		printBoard(board)

