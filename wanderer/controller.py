from maze import Maze
from hero import Hero
from enemies import Enemies



class Controller():

    def __init__(self, canvas):
        self.canvas = canvas
        self.maze = Maze(canvas, self, 0)
        self.hero = Hero(canvas, self)
        self.enemies = Enemies(canvas, self)
        pass



    def next_level(self):
        self.canvas.delete("all")
        self.enemies = Enemies(self.canvas, self)
        self.maze = Maze(self.canvas, self, self.maze.level + 1)
        self.hero.position_row = 1
        self.hero.position_col = 1
        self.hero.has_key = False
        self.hero.heal()
        self.hero.move_character_to(1, 1)