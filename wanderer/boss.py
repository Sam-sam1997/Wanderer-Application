from character import Character
from tkinter import *


class Boss(Character):

    def __init__(self, canvas, controller):
        Character.__init__(self)
        self.canvas = canvas
        self.controller = controller
        self.name = "Boss"
        self.has_key = False
        self.level = self.calculate_level()
        self.image = PhotoImage(file="images/boss.gif")

        self.hp = 2 * self.level * self.d6() + self.d6()
        self.current_hp = self.hp
        self.dp = self.level / 2 * self.d6() + self.d6() / 2
        self.sp = self.level * self.d6() + self.level