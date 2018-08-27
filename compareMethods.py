from nQueensBacktracking import SolveNQueensBacktracking
from nQueensMinConflicts import SolveNQueensMinConflict
from time import clock
if __name__ == '__main__':
	N = int(input("N to compare (Backtracking can take a long time for N > 20):"))

	print("Comparing",N,"Starting with MinConflict:")

	start = clock()
	sol = SolveNQueensMinConflict(N)
	end = clock()

	if (not sol):
		print("MinConflict couldnt find a solution")

	print("MinConflict done",end-start,"seconds")

	print("Starting backtracking...")

	start= clock()
	sol = SolveNQueensBacktracking(N)
	end = clock()

	if (not sol):
		print("Backtracking couldnt find a solution")

	print("backtracking done",end-start,"seconds")
