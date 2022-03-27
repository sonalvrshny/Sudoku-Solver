from collections import defaultdict


class Solution:

    def solveSudoku(grid):
        # grid size is 9 in sudoku
        N = 9

        # define a list of sets for each row, column, box
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        # check if number can be placed in the cell
        def validNumber(value, row, col):
            return not (value in rows[row] or value in columns[col] or value in boxes[calcBox(row, col)])

        # function to define what is the box number
        def calcBox(row, col):
            return (row // 3 ) * 3 + col // 3

        # function to update the sets with numbers which are present on the grid
        def updateSet(value, i, j):
            rows[i][value] += 1
            columns[j][value] += 1
            boxes[calcBox(i, j)][value] += 1
            grid[i][j] = str(value)

        # function to remove from set when have to backtrack
        def removeFromSet(value, row, col):
            del rows[row][value]
            del columns[col][value]
            del boxes[calcBox(row, col)][value]
            grid[row][col] = "."

        # function for calling recursion
        def updateNextNumber(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal solved
                solved = True
            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)


        # recursive function to backtrack the values which can be put into the grid
        def backtrack(row, col):
            if grid[row][col] == ".":
                # iterate thru all possibilities of 1-9
                for i in range(1, N+1):
                    if validNumber(i, row, col):
                        updateSet(i, row, col)
                        updateNextNumber(row, col)
                        if not solved:
                            removeFromSet(i, row, col)
            else:
                updateNextNumber(row, col)


        # iterate over the grid and update the sets with numbers already present on the grid
        for i in range(N):
            for j in range(N):
                if grid[i][j] != ".":
                    updateSet(int(grid[i][j]), i, j)

        solved = False
        backtrack(0, 0)


if __name__== "__main__":
    initialGrid = [["5","3",".",".","7",".",".",".","."],
                   ["6",".",".","1","9","5",".",".","."],
                   [".","9","8",".",".",".",".","6","."],
                   ["8",".",".",".","6",".",".",".","3"],
                   ["4",".",".","8",".","3",".",".","1"],
                   ["7",".",".",".","2",".",".",".","6"],
                   [".","6",".",".",".",".","2","8","."],
                   [".",".",".","4","1","9",".",".","5"],
                   [".",".",".",".","8",".",".","7","9"]]
    Solution.solveSudoku(initialGrid)
    for i in initialGrid:
        print(i)  

