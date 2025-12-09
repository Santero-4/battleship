# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:39:23 2024

@author: lmbe0
"""

import graphics
import random


L = 1200
H = 800

square_size = H//16



phase = 'startup'

# win = graphics.GraphWin("My Window", L, H)

# # Sets the coordinate system
# win.setCoords(0, 0, L, H)

# # changes the background color
# win.setBackground("black")  # <-- comment late

# vals = menu2.init_window()
# win = vals[0]
# difficulty_level = vals[1][1]
# win.setBackground("black")
# win.setCoords(0, 0, L, H)

window = ''
difficulty_level = ''

def drawsquare(a, b, c):
    pnt_a = a
    pnt_b = b
    rec = graphics.Rectangle(pnt_a, pnt_b)
    rec.setFill(c)
    rec.draw(window)
    return (rec)

def makebutton(a, b, c, d, text, button_name, button_lable, bgcolor, text_color, size):
    '''Makes a button box with centered text. 
    a and b are the x and y of the bottom left point, c and d are the x and y of the top right point'''
    button_name = graphics.Rectangle(
        graphics.Point(a, b), graphics.Point(c, d))
    button_name.setFill(bgcolor)
    button_lable = graphics.Text(button_name.getCenter(), text)
    button_lable.setTextColor(text_color)
    button_lable.setSize(size)
    return (button_name, button_lable)

quit_button, quit_lable = makebutton(0,H-50,100,H, 'Quit', "quit_button", "quit_lable", 'red', 'black', 36)


player_grid = []
player_squares = []
def create_player_grid():
    for x in range(10):
        player_grid.append([])
    for row in player_grid:
        for col in range(10):
            row.append('empty')

def print_player_grid():
    for num, row in enumerate(player_grid):
        # print()
        for idx, elem in enumerate(row):
            a = graphics.Point(idx*square_size, num*square_size)
            b = graphics.Point((idx+1)*square_size, (num+1)*square_size)
            if elem == 'player':
                color = 'green1'
            if elem == 'hit':
                color = 'firebrick1'
            if elem == 'empty':
                color = 'dodger blue'
            if elem == 'miss':
                color = 'white'
            if elem == 'repeat':
                color = 'yellow'
            pgsquare = drawsquare(a, b, color)
            player_squares.append(pgsquare)

def reset_player_grid():
     for i in range(10):
         for j in range(10):
             player_grid[i][j] = 'empty'     

def update_player_grid():
    for s in player_squares:
        s.undraw()
    print_player_grid()
    
def delete_everything():
    for s in player_squares:
        s.undraw()
    for a in attack_squares:
        a.undraw()

attack_grid = []
attack_squares = []
def create_attack_grid():
    for x in range(10):
        attack_grid.append([])
    for arow in attack_grid:
        for acol in range(10):
            arow.append('empty')
            
def print_attack_grid():
    for num, arow in enumerate(attack_grid):
        # print()
        for idx, elem in enumerate(arow):
            c = graphics.Point((square_size*14)+(idx*square_size), num*square_size)
            d = graphics.Point((square_size*14)+((idx+1)*square_size), (num+1)*square_size)
            if elem == 'hit':
                color2 = 'firebrick1'
            if elem == 'miss':
                color2 = 'white'
            if elem == 'empty':
                color2 = 'dodger blue'
            if elem == 'enemy':
                color2 = 'dodger blue'
            agsquare = drawsquare(c, d, color2)
            attack_squares.append(agsquare)  
            
def update_attack_grid():
    for a in attack_squares:
        a.undraw()
    print_attack_grid()

def get_square():
    while True:
        locate_this = window.getMouse()
        locate_x = locate_this.getX()//1
        locate_y = locate_this.getY()//1
        # print(locate_x in range(0,1000))
        if locate_x in range(0, 100) and locate_y in range(H-50, H):
            window.close()
        if locate_x in range(0, (1+square_size*10)) and phase == 'startup':
            for i in range(10):
                y_start = square_size*i
                y_end = y_start + square_size
                if locate_y in range(y_start, y_end):
                    for j in range(10):
                        x_start = square_size*j
                        x_end = x_start+square_size
                        if locate_x in range(x_start, x_end):
                            return (y_start//square_size, x_start//square_size, 'player')
        if locate_x in range((square_size*14), (1+square_size*25)) and phase == 'battle':
            for i in range(10):
                y_start = square_size*i
                y_end = y_start + square_size
                if locate_y in range(y_start, y_end):
                    for j in range(10):
                        x_start = (square_size*14)+(square_size*j)
                        x_end = x_start+square_size
                        if locate_x in range(x_start, x_end):
                            return (y_start//square_size, (x_start-(square_size*14))//square_size, 'attack')

def update_square():
    while True:
        location = get_square()
        xcoord = location[1]
        ycoord = location[0]
        grid = location[2]
        if phase == 'startup':
            check_here = player_grid[ycoord][xcoord]
            if grid == 'player':
                if check_here == 'empty':
                    player_grid[ycoord][xcoord] = 'player'
                    break
                if check_here == 'player':
                    player_grid[ycoord][xcoord] = 'empty'
                    break
            if grid == 'attack':
                continue
        if phase == 'battle':
            check_here = attack_grid[ycoord][xcoord]
            if grid == 'player':
                continue
            if grid == 'attack':
                if check_here == 'empty':
                    attack_grid[ycoord][xcoord] = 'miss'
                    break
                if check_here == 'enemy':
                    attack_grid[ycoord][xcoord] = 'hit'
                    break
                if check_here == 'miss' or check_here == 'hit':
                    continue
    update_player_grid()
    return check_here
    

def place_player_ships():
    text_counter = 0
    while True:
        player_ship_count = 0
        placing_instructions = graphics.Text(graphics.Point(L//2, H-100),f'Click to place a ship. Click again to unplace. Ships used: {text_counter} / 15')
        placing_instructions.setTextColor('white')
        placing_instructions.draw(window)
        update_square()
        placing_instructions.undraw()
        for x in range(10):
            player_ship_count += player_grid[x].count('player')
            text_counter = player_ship_count
        if player_ship_count == 15:
            break

def confirm_ship_placement():
       confirm_button, confirm_label = makebutton(
           (L-400)//2, H-200, L//2, H, "START GAME?", 'confirm_button', 'confirm_lable', 'green3', 'white', 15)
       confirm_button.draw(window)
       confirm_label.draw(window)
       reset_button, reset_label = makebutton(L-150, H-H, L, H-600, "RESET", 'reset_button', 'reset_lable', 'red', 'black', 20)
       reset_button.draw(window)
       reset_label.draw(window)
       while True:
           click = window.getMouse()
           clickX = click.getX()//1
           clickY = click.getY()//1
           if clickX in range((L-400)//2, L//2) and clickY in range(H-200, H):
               confirm_button.undraw()
               confirm_label.undraw()
               reset_button.undraw()
               reset_label.undraw()
               return None
           if clickX in range(L-150, L) and clickY in range(H-H, H-600):
               reset_player_grid()
               for s in player_squares:
                   s.undraw()
               print_player_grid()
               place_player_ships()
               
def place_enemy_ships():
    enemy_ship_counter = 0
    if difficulty_level == 'easy':
        while enemy_ship_counter <15:
            occupied = False
            flip = random.randint(0,1)
            if flip == 0:
                i = random.randint(0, 9)
                j = random.randint(0, 4)
                for y in range(5):
                    if attack_grid[i][j + y] == 'enemy':
                        occupied = True
                        break
                for x in range(5):
                    if occupied:
                        break
                    attack_grid[i][j+x] = 'enemy'
                    enemy_ship_counter += 1
            if flip == 1:
                i = random.randint(0, 4)
                j = random.randint(0, 9)
                for y in range(5):
                    if attack_grid[i+y][j] == 'enemy':
                        occupied = True
                        break
                for x in range(5):
                    if occupied:
                        break
                    if attack_grid[i+x][j] != 'enemy':
                        attack_grid[i+x][j] = 'enemy'
                        enemy_ship_counter += 1
    if difficulty_level == 'normal':
        occupied = False
        flip = random.randint(0,1)
        if flip == 0:
            i = random.randint(0, 9)
            j = random.randint(0, 6)
            for x in range(3):
                attack_grid[i][j+x] = 'enemy'
                enemy_ship_counter += 1
        if flip == 1:
            i = random.randint(0, 6)
            j = random.randint(0, 9)
            for x in range(3):
                if attack_grid[i+x][j] != 'enemy':
                    attack_grid[i+x][j] = 'enemy'
                    enemy_ship_counter += 1
        while enemy_ship_counter <15:
            occupied = False
            flip = random.randint(0,1)
            if flip == 0:
                i = random.randint(0, 9)
                j = random.randint(0, 5)
                for y in range(4):
                    if attack_grid[i][j + y] == 'enemy':
                        occupied = True
                        break
                for x in range(4):
                    if occupied:
                        break
                    attack_grid[i][j+x] = 'enemy'
                    enemy_ship_counter += 1
            if flip == 1:
                i = random.randint(0, 5)
                j = random.randint(0, 9)
                for y in range(4):
                    if attack_grid[i+y][j] == 'enemy':
                        occupied = True
                        break
                for x in range(4):
                    if occupied:
                        break
                    if attack_grid[i+x][j] != 'enemy':
                        attack_grid[i+x][j] = 'enemy'
                        enemy_ship_counter += 1
    if difficulty_level == 'hard':
        while enemy_ship_counter <15:
            occupied = False
            flip = random.randint(0,1)
            if flip == 0:
                i = random.randint(0, 9)
                j = random.randint(0, 6)
                for y in range(3):
                    if attack_grid[i][j + y] == 'enemy':
                        occupied = True
                        break
                for x in range(3):
                    if occupied:
                        break
                    attack_grid[i][j+x] = 'enemy'
                    enemy_ship_counter += 1
            if flip == 1:
                i = random.randint(0, 6)
                j = random.randint(0, 9)
                for y in range(3):
                    if attack_grid[i+y][j] == 'enemy':
                        occupied = True
                        break
                for x in range(3):
                    if occupied:
                        break
                    if attack_grid[i+x][j] != 'enemy':
                        attack_grid[i+x][j] = 'enemy'
                        enemy_ship_counter += 1
    print_attack_grid()

attack_here = -10
def do_enemy_attack():
    most_row = player_grid[0]
    for x in range(10):
        ships_in_row = player_grid[x].count('player')
        if ships_in_row > most_row.count('player'):
            most_row = player_grid[x]
    rand_row = random.randint(0, 9)
    rand_col = random.randint(0, 9)
    counter = 0
    if difficulty_level == 'easy':
        if player_grid[rand_row] == most_row:
            fail = random.randint(0, 1)
            if fail == 1:
                if rand_row != 9:
                    rand_row += 1
                elif rand_row == 9:
                    rand_row -= 9
        while player_grid[rand_row][rand_col] == 'miss' or player_grid[rand_row][rand_col] == 'hit':
            if counter%10 !=0:
                if rand_col != 9:
                    rand_col += 1
                    counter += 1
                    print(counter)
                elif rand_col == 9:
                    rand_col -=9
                    counter += 1
                    print(counter)
            elif counter%10 == 0:
                counter+=1
                if rand_row != 9:
                    rand_row += 1
                elif rand_row == 9:
                    rand_row -= 9
        if player_grid[rand_row][rand_col] == 'player':
            player_grid[rand_row][rand_col] = 'hit'
            print_player_grid()
            return -1
        if player_grid[rand_row][rand_col] == 'empty':
            player_grid[rand_row][rand_col] = 'miss'
            print_player_grid()
            return -10
        if player_grid[rand_row][rand_col] == 'miss':
            player_grid[rand_row][rand_col] = 'repeat'
            print_player_grid()
            return -1
    if difficulty_level == 'normal':
        while player_grid[rand_row][rand_col] == 'miss' or player_grid[rand_row][rand_col] == 'hit':
            if counter%10 !=0:
                if rand_col != 9:
                    rand_col += 1
                    counter += 1
                    print(counter)
                elif rand_col == 9:
                    rand_col -=9
                    counter += 1
                    print(counter)
            elif counter%10 == 0:
                counter +=1
                if rand_row != 9:
                    rand_row += 1
                elif rand_row == 9:
                    rand_row -= 9
        if attack_here > 0:
            rand_row = attack_here
        if player_grid[rand_row][rand_col] == 'player':
            player_grid[rand_row][rand_col] = 'hit'
            print_player_grid()
            return rand_row
        if player_grid[rand_row][rand_col] == 'empty':
            player_grid[rand_row][rand_col] = 'miss'
            print_player_grid()
            return -10
    if difficulty_level == 'hard':
        while player_grid[rand_row] != most_row:
            if rand_row != 9:
                rand_row += 1
            elif rand_row == 9:
                rand_row -= 9
        if attack_here >= 0 and attack_here < 9:
            rand_col == attack_here + 1
        hard_fail = random.randint(1, 10)
        if hard_fail > 7:
            if rand_row != 9:
                rand_row += 1
            elif rand_row == 9:
                rand_row -= 9
        while player_grid[rand_row][rand_col] == 'miss' or player_grid[rand_row][rand_col] == 'hit':
            if counter%10 !=0:
                if rand_col != 9:
                    rand_col += 1
                    counter += 1
                    print(counter)
                elif rand_col == 9:
                    rand_col -=9
                    counter += 1
                    print(counter)
            elif counter%10 == 0:
                counter+=1
                if rand_row != 9:
                    rand_row += 1
                elif rand_row == 9:
                    rand_row -= 9
        if player_grid[rand_row][rand_col] == 'player':
            player_grid[rand_row][rand_col] = 'hit'
            print_player_grid()
            return rand_col
        if player_grid[rand_row][rand_col] == 'empty':
            player_grid[rand_row][rand_col] = 'miss'
            print_player_grid()
            return -10
    print_player_grid()
    return -1

def check_win():
   
    player_ship_count = 0
    enemy_ship_count = 0
    if difficulty_level == 'easy':
        battle_text = 'The computer has 3 ships that are 5 sqaures long'
    if difficulty_level == 'normal':
        battle_text = 'The computer has 3 ships that are 4 sqaures long, and 1 that is 3 squares long'
    if difficulty_level == 'hard':
        battle_text = 'The computer has 5 ships that are 3 sqaures long'
    for x in range(10):
        player_ship_count += player_grid[x].count('player')
        enemy_ship_count += attack_grid[x].count('enemy')
    battle_ships = enemy_ship_count
    battle_instructions = graphics.Text(graphics.Point(L//2, H-250), f'{battle_text}. Computer ships remaining: {battle_ships} / 15 ')
    battle_instructions.setTextColor('white')
    if player_ship_count == 0:
        return 2
    elif enemy_ship_count == 0:
        return 1
    else:
        return battle_instructions

bombs = [[],[],[],[]]
def make_bombs(x,y,b):
    for z in range(3):
        bombs[b].append((x+1+z,y+1))
        bombs[b].append((x+1+z,y-1))
    for z in range(5):
        bombs[b].append((x+z,y))
    bombs[b].append((x+2,y+2))
    bombs[b].append((x+2,y-2))
make_bombs(0, 7, 0)
make_bombs(0, 2, 1)
make_bombs(5, 7, 2)
make_bombs(5, 2, 3)
used_bombs = []
used_targets = []

def deploy_special_attack():
    if difficulty_level == 'easy':
        easy_special_fail = random.randint(0, 1)
        print(easy_special_fail)
        if easy_special_fail == 0:
            easy_hit_counter = 0
            full_counter = 0
            while easy_hit_counter <=5:
                randx = random.randint(0,9)
                randy = random.randint(0,9)
                if player_grid[randx][randy] != 'miss':
                    if player_grid[randx][randy] == 'player':
                        player_grid[randx][randy] = 'hit'
                    if player_grid[randx][randy] == 'empty':
                        player_grid[randx][randy] = 'miss'
                    easy_hit_counter +=1
                full_counter += 1
                if full_counter >= 100:
                    break
            update_player_grid()
            return 0
        elif easy_special_fail == 1:
            easy_hit_counter = 0
            full_counter = 0
            while easy_hit_counter <=5:
                randx = random.randint(0,9)
                randy = random.randint(0,9)
                if attack_grid[randx][randy] != 'miss':
                    if attack_grid[randx][randy] == 'enemy':
                        attack_grid[randx][randy] = 'hit'
                    if attack_grid[randx][randy] == 'empty':
                        attack_grid[randx][randy] = 'miss'
                    easy_hit_counter +=1
                full_counter += 1
                if full_counter >= 100:
                    break
            update_attack_grid()
            return 1
    if difficulty_level == 'normal':
        bomb = random.randint(0,3)
        anchors = [(400, 150), (150, 150), (400, 400), (150, 400)]
        if bomb in used_bombs:
            fail = 1
            expl = -1
        else:
            fail = 0
            anch = anchors[bomb]
            x = anch[0]
            y= anch[1]
            expl = graphics.Image(graphics.Point(x, y), 'explosion_small.png')
        for location in bombs[bomb]:
            if player_grid[location[0]][location[1]] == 'player':
                player_grid[location[0]][location[1]] = 'hit'
            elif player_grid[location[0]][location[1]] == 'empty':
                player_grid[location[0]][location[1]] = 'miss'
        update_player_grid()
        used_bombs.append(bomb)
        return(fail, expl)
    if difficulty_level == 'hard':
        target = random.randint(0,9)
        if target in used_targets:
            fail = 1
        else: 
            fail= 0
        for x in range(10):
            if player_grid[target][x] == 'player':
                player_grid[target][x] = 'hit'
            elif player_grid[target][x] == 'empty':
                player_grid[target][x] = 'miss'
        update_player_grid()
        used_targets.append(target)
        return(fail)

def display_diff_text():
    inst_text = graphics.Text(graphics.Point(L//4, H-750),'Click anywhere to advance.')
    inst_text.setTextColor('white')
    if difficulty_level == 'easy':
        diff_text1 = 'Your opponent is the most highly adaptable team of soldiers in the world......'
        diff_text2 = 'The green army men....!'
        draw_text1 = graphics.Text(graphics.Point(L//2, H-100),diff_text1)
        draw_text2 = graphics.Text(graphics.Point(L//2, H-700),diff_text2)
        diff_image = graphics.Image(graphics.Point(L//2,H//2),'armymen.png')
    if difficulty_level == 'normal':
        diff_text1 = 'Your opponent is world\'s most memed nuclear scientist......'
        diff_text2 = 'Dr. Robert J. Oppenhiemer....!'
        draw_text1 = graphics.Text(graphics.Point(L//2, H-100),diff_text1)
        draw_text2 = graphics.Text(graphics.Point(L//2, H-700),diff_text2)
        diff_image = graphics.Image(graphics.Point(L//2,H//2),'Oppie.png') 
    if difficulty_level == 'hard':
        diff_text1 = 'Your opponent is WWII\'s greatest naval strategist......'
        diff_text2 = 'Sir Winston Churchill....!'
        draw_text1 = graphics.Text(graphics.Point(L//2, H-100),diff_text1)
        draw_text2 = graphics.Text(graphics.Point(L//2, H-700),diff_text2)
        diff_image = graphics.Image(graphics.Point(L//2,H//2),'churchill_unlaseredtall.png')
    draw_text1.setTextColor('white')
    draw_text2.setTextColor('white')
    inst_text.draw(window)
    draw_text1.draw(window)
    window.getMouse()
    diff_image.draw(window)
    window.getMouse()
    draw_text2.draw(window)
    window.getMouse()
    inst_text.undraw()
    draw_text1.undraw()
    draw_text2.undraw()
    diff_image.undraw()
    
def display_battle_chars(turns, special, last, fail, last_use, bomb):
    global char_drawn
    if type(last_use) != int:
        return -1
    pships = 0 
    eships = 0
    talk_box = graphics.Rectangle(graphics.Point(L-700, H), graphics.Point(L-300, H-150))
    anchor = talk_box.getCenter()
    talk_box.setOutline('firebrick1')
    talk_box.setFill('black')
    talk_box.setWidth('3')
    for x in range(10):
        pships += player_grid[x].count('player')
        eships += attack_grid[x].count('enemy')
    if difficulty_level == 'easy':
        pic = 'army_small.png'
        vox_ehit = 'Another one bites the dust!'
        vox_emiss = "We'll get it next time!"
        vox_pmiss = "You'll NEVER sink our ships!"
        vox_phit = "Noooo!! Our beautiful ships!"
        spvox_win = 'Here comes the cavalry!!'
        spvox_fail = 'Tactical retreat!'            
    if difficulty_level == 'normal':
        pic = 'Oppie_small.png'
        vox_ehit = 'Brilliance never goes to waste.'
        vox_emiss = "Hrm... Miscalculated..."
        vox_pmiss = "As expected."
        vox_phit = "The probability of this was near zero."
        spvox_win = 'I am become Death, destroyer of worlds....'
        spvox_fail = 'The mysteries of the atom elude me....For now.' 
    if difficulty_level == 'hard':
        pic = 'Churchill_unlasered.png'
        vox_ehit = 'Superior strategy.'
        vox_emiss = "A flaw in the plan...Unacceptable."
        vox_pmiss = "You need a strategy."
        vox_phit = "You are proving to be... A most interesting opponent. "
        spvox_win = 'Face the power of my Great Britain Beam!'
        spvox_fail = 'Hmph... Consider yourself lucky...' 
    if not special:
        if last == 'phit' and turns%5 == 0:
            v = vox_phit
        elif last == 'pmiss' and turns%7 == 0:
            v = vox_pmiss
        elif last == 'ehit' and turns%3 == 0:
            v = vox_ehit
        elif last == 'emiss' and turns%8 == 0:
            v = vox_emiss
        else:
            return -1
    if special:
        if fail == 0:
            v = spvox_win
        if fail == 1:
            v = spvox_fail
    vox = graphics.Text(anchor, v)
    char = graphics.Image(graphics.Point(L-150, H-150),pic)
    char.draw(window)
    vox.setTextColor('white')
    talk_box.draw(window)
    vox.draw(window)
    if type(bomb) != int:
        bomb.draw(window) 
    window.getMouse
    talk_box.undraw()
    vox.undraw()
    char.undraw()
    return [bomb, vox, talk_box, char]




















            