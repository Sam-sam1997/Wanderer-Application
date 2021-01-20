import random
from skeleton import Skeleton
from boss import Boss



class Enemies():

    def __init__(self, canvas, controller):
        self.canvas = canvas
        self.enemies = []
        self.controller = controller

        self.enemies.append(Boss(self.canvas, self.controller))

        for i in range(random.randint(2, 5)):
            if i == 0:
                self.enemies.append(Skeleton(self.canvas, self.controller, True))
            else:
                self.enemies.append(Skeleton(self.canvas, self.controller, False))

        for i in self.enemies:
            i.draw(self.canvas, self.controller.maze)

    # getter for enemy at specific position
    def get_enemy_at(self, row, col):

        for i in self.enemies:
            if i.position_row == row and i.position_col == col:
                return i

        return False

    def get_boss(self):
        return self.enemies[0]

    def move_enemies(self):
        for i in self.enemies:
            move = i.find_valid_moves()
            i.move_character_to(move[0], move[1])

    def hide_enemies(self):
        for i in self.enemies:
            i.hide_from_maze()

    def draw_enemies(self):
        for i in self.enemies:
            i.move_character_to(i.position_row, i.position_col)