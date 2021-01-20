from tkinter import *
from controller import Controller
from tkinter.font import Font
import random

root = Tk()
canvas = Canvas(root, width=720, height=720)

ctr = Controller(canvas)
var1 = StringVar()
var1.set(ctr.hero.display_stats())


# User input handler
def on_key_press(e):
    if not ctr.hero.is_fighting:
        current_pos = ctr.hero.get_hero_position()

        if e.keycode == 87 or e.keycode == 38:
            # upper case
            ctr.hero.hide_from_maze()
            ctr.hero.move_character_to(ctr.hero.position_row - 1, ctr.hero.position_col)
            ctr.hero.number_of_moves += 1

            if ctr.hero.number_of_moves % 2 == 0:
                ctr.enemies.hide_enemies()
                ctr.hero.move_character_to(ctr.hero.position_row, ctr.hero.position_col)
                ctr.enemies.move_enemies()

        elif e.keycode == 83 or e.keycode == 40:
            # down
            ctr.hero.hide_from_maze()
            ctr.hero.move_character_to(ctr.hero.position_row + 1, ctr.hero.position_col)
            ctr.hero.number_of_moves += 1

            if ctr.hero.number_of_moves % 2 == 0:
                ctr.enemies.hide_enemies()
                ctr.hero.move_character_to(ctr.hero.position_row, ctr.hero.position_col)
                ctr.enemies.move_enemies()

        elif e.keycode == 68 or e.keycode == 39:
            # right
            ctr.hero.hide_from_maze()
            ctr.hero.move_character_to(ctr.hero.position_row, ctr.hero.position_col + 1)
            ctr.hero.number_of_moves += 1

            if ctr.hero.number_of_moves % 2 == 0:
                ctr.enemies.hide_enemies()
                ctr.hero.move_character_to(ctr.hero.position_row, ctr.hero.position_col)
                ctr.enemies.move_enemies()
        elif e.keycode == 65 or e.keycode == 37:
            # left
            ctr.hero.hide_from_maze()
            ctr.hero.move_character_to(ctr.hero.position_row, ctr.hero.position_col - 1)
            ctr.hero.number_of_moves += 1

            if ctr.hero.number_of_moves % 2 == 0:
                ctr.enemies.hide_enemies()
                ctr.hero.move_character_to(ctr.hero.position_row, ctr.hero.position_col)
                ctr.enemies.move_enemies()
    else:
        if e.keycode == 32:
            enemy = enemy = ctr.enemies.get_enemy_at(ctr.hero.position_row, ctr.hero.position_col)
            ctr.hero.strike(enemy)
            boss = ctr.enemies.get_boss()

            if enemy.current_hp <= 0:
                ctr.enemies.enemies.remove(enemy)
                ctr.hero.is_fighting = False
                ctr.hero.level_up()

                if enemy.has_key:
                    ctr.hero.has_key = True

                if ctr.hero.has_key and boss.current_hp <= 0:
                    ctr.next_level()
            else:
                enemy.strike(ctr.hero)
                if ctr.hero.current_hp <= 0:
                    quit()

    if ctr.enemies.get_enemy_at(ctr.hero.position_row, ctr.hero.position_col) != False:
        enemy = ctr.enemies.get_enemy_at(ctr.hero.position_row, ctr.hero.position_col)
        enemy_stat = enemy.display_stats()
        hero_stat = ctr.hero.display_stats()
        var1.set(hero_stat + "\t" + enemy_stat)
        ctr.hero.is_fighting = True
    else:
        hero_stat = ctr.hero.display_stats()
        var1.set(hero_stat)


canvas.bind("<KeyPress>", on_key_press)

my_font = Font(family="Times New Roman", size=10, weight="bold")
label_hero = Label(root, textvariable=var1, anchor=S, font=my_font)

canvas.pack()
label_hero.pack()

canvas.focus_set()

root.mainloop()