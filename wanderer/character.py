import random


# characters class
class Character():

    def __init__(self):
        self.hp = 0
        self.sp = 0
        self.level = 0
        self.position_row = 0
        self.position_col = 0
        self.dp = 0
        self.current_hp = 0


    def d6(self):
        return random.randint(1, 6)


    def find_empty_cell(self, maze):

        done = False
        i = 0
        j = 0

        while not done:
            i = random.randint(1, 10)
            j = random.randint(1, 10)

            if i == 1 and j == 1:
                continue

            if maze.layout[i][j] == 0:
                done = True
                maze.layout[i][j] = 2

        return [j, i]


    def draw(self, canvas, maze):
        i, j = self.find_empty_cell(maze)
        canvas.create_image((i - 1) * 72 + 36, (j - 1) * 72 + 36,
                            image=self.image)
        self.position_col = i
        self.position_row = j


    def display_stats(self):

        stats = self.name + " (Level " + str(self.level) + ") HP: " + str(self.current_hp) + "/" + str(
            self.hp) + " | DP: " + str(self.dp) + " | SP: " + str(self.dp)

        if self.name == "Boss":
            return stats
        else:
            return stats + " | Key: " + str(self.has_key)


    def calculate_level(self):
        i = random.randint(0, 9)
        chance1 = [0, 1, 2, 3, 4]
        chance2 = [5, 6, 7, 8]

        if i in chance1:
            return self.controller.maze.level
        elif i in chance2:
            return self.controller.maze.level + 1
        else:
            return self.controller.maze.level + 2


    def strike(self, defender):
        strike_value = 2 * self.d6() + self.sp
        if strike_value > defender.dp:
            defender.current_hp -= (strike_value - defender.dp)


    def move_character_to(self, row, col):

        # down
        if row == self.position_row + 1:
            if self.controller.maze.layout[self.position_row + 1][self.position_col] != 1:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row) * 72 + 36,
                                         image=self.image)
                self.position_row = row
            else:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image)

        # up
        if row == self.position_row - 1:
            if self.controller.maze.layout[self.position_row - 1][self.position_col] != 1:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 2) * 72 + 36,
                                         image=self.image)
                self.position_row = row
            else:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image)

        # left
        if col == self.position_col - 1:
            if self.controller.maze.layout[self.position_row][self.position_col - 1] != 1:
                self.canvas.create_image((self.position_col - 2) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image)
                self.position_col = col
            else:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image)

        # right
        if col == self.position_col + 1:
            if self.controller.maze.layout[self.position_row][self.position_col + 1] != 1:
                self.canvas.create_image((self.position_col) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image)
                self.position_col = col
            else:
                self.canvas.create_image((self.position_col - 1) * 72 + 36, (self.position_row - 1) * 72 + 36,
                                         image=self.image)


    def find_valid_moves(self):
        correct_moves = []

        if self.controller.maze.layout[self.position_row + 1][self.position_col] != 1:
            correct_moves.append([self.position_row + 1, self.position_col])
        if self.controller.maze.layout[self.position_row - 1][self.position_col] != 1:
            correct_moves.append([self.position_row - 1, self.position_col])
        if self.controller.maze.layout[self.position_row][self.position_col + 1] != 1:
            correct_moves.append([self.position_row, self.position_col + 1])
        if self.controller.maze.layout[self.position_row][self.position_col - 1] != 1:
            correct_moves.append([self.position_row, self.position_col - 1])

        return correct_moves[random.randint(0, len(correct_moves) - 1)]


    def hide_from_maze(self):
        self.controller.maze.draw_cell(self.position_row, self.position_col)