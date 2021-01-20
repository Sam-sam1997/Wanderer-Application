from tkinter import *


class Maze():

    def __init__(self, canvas, controller, level):
        self.canvas = canvas
        self.level = level
        self.controller = controller
        self.wall = PhotoImage(file="images/wall.gif")
        self.hero = PhotoImage(file="images/hero-down.gif")
        self.floor = PhotoImage(file="images/floor.gif")
        self.layout = []

        self.init_layout()
        self.draw_maze()

    def draw_maze(self):

        for i in range(1, 11):
            for j in range(1, 11):
                self.draw_cell(i, j)

    def init_layout(self):
        for i in range(0, 12):
            temp = []
            for j in range(0, 12):
                if i == 0 or i == 11 or j == 0 or j == 11:
                    temp.append(1)
                else:
                    temp.append(0)
            self.layout.append(temp)

        self.default_map()

    def default_map(self):
        self.layout[1][4] = 1
        self.layout[2][4] = 1
        self.layout[2][6] = 1
        self.layout[2][8] = 1
        self.layout[2][9] = 1
        self.layout[3][2] = 1
        self.layout[3][3] = 1
        self.layout[3][4] = 1
        self.layout[3][6] = 1
        self.layout[3][8] = 1
        self.layout[3][9] = 1
        self.layout[4][6] = 1
        self.layout[5][1] = 1
        self.layout[5][2] = 1
        self.layout[5][3] = 1
        self.layout[5][4] = 1
        self.layout[5][6] = 1
        self.layout[5][7] = 1
        self.layout[5][8] = 1
        self.layout[5][9] = 1
        self.layout[6][2] = 1
        self.layout[6][4] = 1
        self.layout[7][2] = 1
        self.layout[7][4] = 1
        self.layout[7][6] = 1
        self.layout[7][7] = 1
        self.layout[7][9] = 1
        self.layout[8][6] = 1
        self.layout[8][7] = 1
        self.layout[8][9] = 1
        self.layout[9][2] = 1
        self.layout[9][3] = 1
        self.layout[9][4] = 1
        self.layout[9][9] = 1
        self.layout[10][4] = 1
        self.layout[10][6] = 1
        self.layout[10][7] = 1


    def draw_cell(self, col, row):
        if self.layout[col][row] == 1:
            self.canvas.create_image((row - 1) * self.wall.width() + self.wall.width() / 2,
                                     (col - 1) * self.wall.width() + self.wall.width() / 2, image=self.wall)
        else:
            self.canvas.create_image((row - 1) * self.floor.width() + self.floor.width() / 2,
                                     (col - 1) * self.floor.width() + self.floor.width() / 2, image=self.floor)