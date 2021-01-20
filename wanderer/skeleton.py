from character import Character
from tkinter import *


class Skeleton(Character):

    def __init__(self, canvas, controller, key):
        Character.__init__(self)
        self.canvas = canvas
        self.controller = controller
        self.image = PhotoImage(file="images/skeleton.gif")
        self.name = "Skeleton"
        self.level = self.calculate_level()
        self.has_key = key

        self.hp = 2 * self.level * self.d6()
        self.current_hp = self.hp
        self.dp = self.level / 2 * self.d6()
        self.sp = self.level * self.d6()