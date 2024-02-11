import tkinter as tk
import time
import numpy as np
import os
out_txt = open("output.txt", "w")
class search_tree:
    def __init__(self, data):
        self.data = data
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)
    def get_children(self):
        return self.children
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
def expand_children(search_tree):
    children = []
    # code to get children 
    return children
def heuristic(search_tree):
    childrens = search_tree.get_children()
    # code to get heuristics
    heuristics = []
    return heuristics
def cost_function(search_tree):
    childrens = search_tree.get_children()
    # code to get cost
    cost = []
    return cost
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, data):
        self.stack.append(data)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
class QueensBoardGUI:
    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[0] * board_size for _ in range(board_size)]

        self.root = tk.Tk()
        self.root.title("8 Queens Puzzle")
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")

        cell_size = 400 // self.board_size

        for row in range(self.board_size):
            for col in range(self.board_size):
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                if self.board[row][col] == 1:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="gray")
                    self.canvas.create_text(x1 + cell_size // 2, y1 + cell_size // 2, text="Q", font=("Arial", 12))
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")

    def place_queen(self, row, col):
        self.board[row][col] = 1
        self.draw_board()

    def remove_queen(self, row, col):
        self.board[row][col] = 0
        self.draw_board()
    
    def queens_placed(self):
        placed = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 1:
                   placed.append((i,j))
        return placed 

    def run(self):
        self.root.mainloop()

    def run(self):
        self.root.after(100, self.root.quit)
        self.root.mainloop()
def place_check(board, x, y):
    placed = board.queens_placed()
    if len(placed) == 0:
        return True
    for i in placed:
        if i[0] == x or i[1] == y: # same row or column
            return False
        if i[0] - i[1] == x-y: # same diagonal
            return False 
        if i[0] + i[1] == x+y:  # same diagonal
            return False
        
    return True

class dfs_solver:
    def __init__(self):
        self.board = QueensBoardGUI(8)
        self.board_list = Stack() 
        self.arr = []
        self.node_explored = 0
        self.res = []
        self.max_space = 0;

    def get_places(self, arr):
        places = []
        for i in range(8):
            for j in range(8):
                if (i,j) not in arr:
                    places.append((i,j))
        return places
    
    def place_checker(self, arr, x, y):
        placed = arr
        if len(placed) == 0:
            return True
        for i in placed:
            if i[0] == x or i[1] == y:
                return False;
            if i[0] -i[1] == x-y:
                return False;
            if i[0] +i[1] == x+y:
                return False
        return True;

    def goal_check(self, arr):
        if len(arr) == 8:
            return True;
        return False;
    def expansion_dfs(self, arr):
        board_list = []
        for i in self.get_places(arr):
            if self.place_checker(arr, i[0], i[1]):
                temp_board_list = []
                for x in arr:
                    temp_board_list.append(x)
                temp_board_list.append(i)
                board_list.append(temp_board_list)
        return board_list
        
    def solve_by_dfs(self):
        self.board.place_queen(0,0)
        print("start", self.board.queens_placed())
        self.board_list.push([(0,0)])
        with open("output.txt", "w") as f:
            while not self.board_list.is_empty():
                if len(self.board_list.stack) > self.max_space:
                    self.max_space = len(self.board_list.stack)
                temp = self.board_list.pop()
                for j in self.expansion_dfs(temp):
                    self.node_explored += 1
                    f.write(str(j) + "\n")
                    if self.goal_check(j):
                        return j;
                    self.board_list.push(j)
            return False
dfs_solve = dfs_solver()
dfs_solve.res = dfs_solve.solve_by_dfs()
print("result : ", dfs_solve.res)
print("nodes explored : ", dfs_solve.node_explored)
print("space currently using : ", len(dfs_solve.board_list.stack))
print("max space used : ", dfs_solve.max_space)
