import numpy as np
import random
import os
import sys

PATH = os.path.join("D:\\","Python","Games","Pygame",
                    "Sudoku","Solutions.txt")

def validate_board(board,verbose):
    for num in range(1,10):
        #Check row
        for i, row in enumerate(board):
            if row.count(num) > 1:
                if verbose:
                    print(f"There are multiple {num}s in row {i+1}")
                return False
        #Check column
        for i in range(9):
            column_nums = []
            for j in range(9):
                column_nums.append(board[j][i])
            if column_nums.count(num) > 1:
                if verbose:
                    print(f"There are multiple {num}s in column {i+1}")
                return False
        #Check box        
        boxes = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for index, pos in enumerate(boxes):
            box_x = pos[1] // 3
            box_y = pos[0] // 3
            box_nums = []
            for i in range(box_y*3, box_y*3+3):
                for j in range(box_x*3, box_x*3+3):
                    box_nums.append(board[i][j])
            if box_nums.count(num) > 1:
                if verbose:
                    print(f"There are multiple {num}s in box {index + 1}")
                return False 
    return True

def check_if_solution():
    #Works out if there was a valid solution
    with open(PATH,"r") as file:
        solution = file.read()
        if not solution:
            return False
        return True

def find_all_filled(board):
    total = 0
    for row in board:
        total += row.count(0)
    return 81 - total

class SolveBoard:

    def __init__(self,board,verbose=None):
        self.verbose = verbose
        if verbose == None:
            self.verbose = False
        self.solved = False
        self.board = board
        with open(PATH,"w") as file:
            file.write("")
        if validate_board(self.board,True) == True:
            if self.verbose:
                self.print_board(self.board)
            self.solve()
            if check_if_solution() == False:
                if self.verbose:
                    print("Tried every permutation, could not find a solution to that board.")

    def validate_pos(self,row,col,num,board=None):
        #Check box
        if not board:
            board = self.board
        self.box_row = row // 3
        self.box_col = col // 3
        for i in range(0,3):
            for j in range(0,3):
                if board[self.box_row*3+j][self.box_col*3+j] == num:
                    return False
        #Check row
        for i in range(9):
            if board[row][i] == num:
                return False
        #Check column 
        for i in range(9):
            if board[i][col] == num:
                return False
        return True 

    def print_board(self,board=None):
        if board == None:
            board = self.board
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("---------------------")
            for j in range(len(board[0])):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                if j == 8:
                    print(board[i][j])
                else:
                    print(str(board[i][j]) + " ", end="")

    def solve(self):
        if self.solved == True:
            return None
        #Pick square
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    #Try numbers 1-9
                    for n in range(1,10):
                        if self.validate_pos(i,j,n) == True:
                            self.board[i][j] = n
                            #Call function again
                            self.solve()
                            self.board[i][j] = 0
                    return None
        if validate_board(self.board,False) == True:
            if self.verbose:
                print("\nSolution:")
                self.print_board(self.board)
                print("")
            self.write_solution()
            self.solved = True

    def write_solution(self,board=None):
        if board == None:
            board = self.board
        with open(PATH,"w") as file:
            file.write("\nSolution:")
            for row in board:
                file.write("\n"+str(row)[1:-1])

class GenerateBoard:

    def __init__(self,level,verbose=None):
        self.verbose = verbose
        if verbose == None:
            self.verbose = False
        self.level = level
        self.generated = False
        if type(level) != int:
            raise TypeError(f"Difficulty level must be type 'int', not type '{type(level)}'")
        if not level in [1,2,3]:
            raise IndexError("Difficulty level must be between 1 and 3")
        self.create_board()
        self.generate()    
        if self.verbose:
            print(f"Currently there are {find_all_filled(self.board)} squares filled in.")
        self.randomize()
        if self.verbose:
            self.solve.print_board(self.board)
    
    def generate(self):
        for times in range(int(self.level * 2)):
            self.remove_nums()        
            self.solve = SolveBoard(self.board,False)
            if check_if_solution() == False:    
                if self.verbose:
                    print("Generating new board")
                self.create_board()
                self.generate()
    
    def List(self):
        self.board = [list(row) for row in self.board]
        return self.board

    def create_board(self):
        self.board1 = [[2,4,6,8,5,7,9,1,3], 
                       [1,8,9,6,4,3,2,7,5],
                       [5,7,3,2,9,1,4,8,6],
                       [4,1,8,3,2,9,5,6,7],
                       [6,3,7,4,8,5,1,2,9],
                       [9,5,2,1,7,6,3,4,8],
                       [7,6,4,5,3,2,8,9,1],
                       [3,2,1,9,6,8,7,5,4],
                       [8,9,5,7,1,4,6,3,2]]

        self.board2 = [[7,8,5,4,3,9,1,2,6],
                       [6,1,2,8,7,5,3,4,9],
                       [4,9,3,6,2,1,5,7,8],
                       [8,5,7,9,4,3,2,6,1],
                       [2,6,1,7,5,8,9,3,4],
                       [9,3,4,1,6,2,7,8,5],
                       [5,7,8,3,9,4,6,1,2],
                       [1,2,6,5,8,7,4,9,3],
                       [3,4,9,2,1,6,8,5,7]]        

        self.board = random.choice((self.board1,self.board2))
        self.randomize()

    def randomize(self):
        self.scramble()
        for times in range(random.randint(1,3)):
            self.board = list(zip(*self.board[::-1]))
            self.scramble()

    def remove_nums(self):
        for row in range(len(self.board)):
            self.board[row] = list(self.board[row])
            for times in range(random.randint(1,2)):    
                self.board[row][random.randint(1,8)] = 0

    def scramble(self):
        self.new_board = []
        #Randomize rows
        self.top_rows = self.board[0:3] 
        self.top_rows = random.sample(self.top_rows,len(self.top_rows))
        for i in self.top_rows:
            self.new_board.append(i)
        self.middle_rows = self.board[3:6]
        self.middle_rows = random.sample(self.middle_rows,len(self.middle_rows))
        for i in self.middle_rows:
            self.new_board.append(i)
        self.bottom_rows = self.board[6:9] 
        self.bottom_rows = random.sample(self.bottom_rows,len(self.bottom_rows))
        for i in self.bottom_rows:
            self.new_board.append(i)
        self.board = self.new_board
    
if __name__ == "__main__":
    board = []
    for i in range(9):
        board.append([0]*9)
    SolveBoard(board,verbose=True)
