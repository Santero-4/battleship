# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:10:19 2024

@author: lmbe0
"""

import engine
import menu2
import Fileio_module
import graphics
import time


def main():
    filename = 'highscores,txt'
    high_scores = Fileio_module.read_high_scores(filename)
    vals = menu2.init_window()
    win = vals[0]
    engine.window = win
    menu2.window = win
    engine.difficulty_level = vals[1][1]
    name = vals[1][0]
    win.setBackground("black")
    win.setCoords(0, 0, engine.L, engine.H)
    
    # expl = graphics.Image(graphics.Point(engine.L//2, engine.H//2),'explosion.png')
    # names = Fileio_module.read_recent_players('recent_players.txt')
    # namesss = graphics.Text(graphics.Point(engine.L//2, engine.H//2),f"{names}")
    # namesss.setTextColor('white')
    # namesss.draw(win)
    
    engine.display_diff_text()    
    
    engine.create_player_grid()
    engine.create_attack_grid()
    engine.print_player_grid()
    engine.quit_button.draw(win)
    engine.quit_lable.draw(win)
    
    engine.place_player_ships()
    engine.confirm_ship_placement()
    engine.place_enemy_ships()
    engine.print_attack_grid()
    engine.phase = 'battle'
    engine.special_charger = 0
    turn_count = 0
    last_use = -1
    expl = -1
    while type(engine.check_win()) != int :
        check = engine.check_win()
        check.draw(win)
        turn_count += 1
        p = engine.update_square()
        print(p)
        if type(expl) != int:
            expl.undraw()
        engine.update_attack_grid()
        if p == 'empty':
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
            last_use = engine.display_battle_chars(turn_count, False, 'pmiss', -1, 0, -1)
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
        elif p == 'enemy':
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
            last_use = engine.display_battle_chars(turn_count, False, 'phit', -1, 0, -1)
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
        engine.attack_here = engine.do_enemy_attack()
        if engine.attack_here == -10:
            engine.special_charger += engine.attack_here
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
            last_use = engine.display_battle_chars(turn_count, False, 'emiss', -1, last_use, -1)
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
        elif engine.attack_here != -10:
            engine.special_charger = 0
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
            last_use = engine.display_battle_chars(turn_count, False, 'ehit', -1, last_use, -1)
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        last_use[x].undraw()
        if engine.special_charger  == -50 and engine.difficulty_level == 'normal':
            engine.special_charger = 0 
            fail2 = engine.deploy_special_attack()
            if type(fail2) != int:
                fail = fail2[0]
                bomb = fail2[1]
            else:
                bomb = fail
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
            last_use = engine.display_battle_chars(turn_count, True,-1,fail, 0, bomb)
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
                if type(last_use[0]) != int:
                    expl = last_use[0]
        elif engine.special_charger  == -40 and engine.difficulty_level != 'normal':
            engine.special_charger = 0 
            fail = engine.deploy_special_attack()
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
            last_use = engine.display_battle_chars(turn_count, True,-1, fail, 0, -1)
            if type(last_use) != int:
                tend = time.time()
                if tend - last_use[4] >3:
                    for x in range(4):
                        if type(last_use[x]) != int:
                            last_use[x].undraw()
        check.undraw()
    if engine.check_win() == 2:
        print('YOU LOSE')
        menu2.lose_screen(win)
        score = 0
    if engine.check_win() == 1:
        menu2.win_screen(win)
        print('YOU WIN')
        remaining_ships = 0
        for x in range(10):
            remaining_ships += engine.player_grid[x].count('player')
            print(remaining_ships)
        remaining_ships = (remaining_ships/15)*100
        print(remaining_ships)
        print(turn_count)
        if engine.difficulty_level == 'easy':
            difficulty = 0.7
        elif engine.difficulty_level == 'normal':
            difficulty = 3
        elif engine.difficulty_level == 'hard':
            difficulty = 12
        score = int(Fileio_module.calculate_score(difficulty, turn_count, remaining_ships))
    high_scores = Fileio_module.update_high_scores(high_scores, name, score)
    print(score)
    print(high_scores)
    Fileio_module.write_high_scores(filename, high_scores)
    engine.delete_everything()
    if type(last_use) != int:
        for x in range(4):
            if type(last_use[x]) != int:
                last_use[x].undraw()
    you_win = graphics.Text(graphics.Point((engine.L//2),engine.H-200),f"{name}:    {score} points!")
    you_win.setTextColor('pink')
    you_win.setSize(36)
    you_win.draw(win)
    i = 500
    for item in high_scores.items():
        win_list = graphics.Text(graphics.Point(engine.L//2, engine.H-i), f"{item[0]}:   {item[1]} points")
        win_list.setTextColor('pink')
        win_list.setSize(36)
        win_list.draw(win)
        i+=50
    win.getMouse()
    win.close()
    



if __name__ == "__main__":
    main()
    
