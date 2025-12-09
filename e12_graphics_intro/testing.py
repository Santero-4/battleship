# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:33:53 2024

@author: lmbe0
"""

import graphics
import random
# import menu2

L = 1200
H = 800

square_size = H//16

# creates the canvass window for the graphics
# win = graphics.GraphWin("My Window", L, H)

# Sets the coordinate system
# win.setCoords(0, 0, L, H)

# changes the background color
# win.setBackground("black")  # <-- comment late





def main():
    global L, H, square_size
    difficulty_level = 'easy'
    # vals = menu2.main()
    # print(vals)
    # difficulty_level = vals[1]

    phase = 'startup'
    # win = menu2.init_window()
    # creates the canvass window for the graphics
    win = graphics.GraphWin("My Window", L, H)

    # # Sets the coordinate system
    win.setCoords(0, 0, L, H)

    # # changes the background color
    win.setBackground("black")  # <-- comment late
    
    
    
    def drawsquare(a, b, c):
        pnt_a = a
        pnt_b = b
        rec = graphics.Rectangle(pnt_a, pnt_b)
        rec.setFill(c)
        rec.draw(win)
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
    quit_button, quit_lable = makebutton(L-200, H-200, L, H, 'Quit', "quit_button", "quit_lable", 'blue', 'white', 36)

    
    # quit_button.draw(win)
    # quit_lable.draw(win)

    # def quit_game():
    #     quit_click = win.getMouse()
    #     quitX = quit_click.getX()//1
    #     quitY = quit_click.getY()//1
    #     if quitX in range(L-200, L+1) and quitY in range(H-200, H+1):
    #         win.close()
    #     else:
    #         pass

    player_grid = []

    def create_player_grid():
        for x in range(10):
            player_grid.append([])
        for row in player_grid:
            for col in range(10):
                # if col%5 == 0:
                #     row.append('player')
                # elif col%7 == 0:
                #     row.append('enemy')
                # else:
                row.append('empty')
        # print(player_grid)
        # player_grid[6][7] = 'hit'
    create_player_grid()

    def reset_player_grid():
        for i in range(10):
            for j in range(10):
                player_grid[i][j] = 'empty'

    def update_player_grid():
        for s in player_squares:
            s.undraw()
        print_player_grid()
        
    attack_grid = []
    def update_attack_grid():
        for a in attack_squares:
            a.undraw()
        print_attack_grid()

    

    def create_attack_grid():
        for x in range(10):
            attack_grid.append([])
        for arow in attack_grid:
            for acol in range(10):
                # if col%5 == 0:
                #     row.append('player')
                # elif col%7 == 0:
                #     row.append('enemy')
                # else:
                arow.append('empty')
        # print(attack_grid)
        # attack_grid[6][7] = 'miss'
    create_attack_grid()

    player_squares = []

    def print_player_grid():
        for num, row in enumerate(player_grid):
            # print()
            for idx, elem in enumerate(row):
                # print(idx*25,num*25, end=" ")
                a = graphics.Point(idx*square_size, num*square_size)
                b = graphics.Point((idx+1)*square_size, (num+1)*square_size)
                if elem == 'player':
                    color = 'green3'
                if elem == 'hit':
                    color = 'red'
                if elem == 'empty':
                    color = 'blue4'
                if elem == 'miss':
                    color = 'white'
                if elem == 'repeat':
                    color = 'yellow'
                pgsquare = drawsquare(a, b, color)
                player_squares.append(pgsquare)

    attack_squares = []

    def print_attack_grid():
        for num, arow in enumerate(attack_grid):
            # print()
            for idx, elem in enumerate(arow):
                # print(300+(idx*25),num*25, end=" ")
                c = graphics.Point(
                    (square_size*11)+(idx*square_size), num*square_size)
                d = graphics.Point(
                    (square_size*11)+((idx+1)*square_size), (num+1)*square_size)
                if elem == 'hit':
                    color2 = 'red'
                if elem == 'miss':
                    color2 = 'white'
                if elem == 'empty':
                    color2 = 'blue4'
                if elem == 'enemy':
                    color2 = 'blue4'
                agsquare = drawsquare(c, d, color2)
                attack_squares.append(agsquare)

    print_player_grid()
    # print_attack_grid()

    def get_square():
        while True:
            locate_this = win.getMouse()
            locate_x = locate_this.getX()//1
            locate_y = locate_this.getY()//1
            # print(locate_x in range(0,1000))
            if locate_x in range(0, (1+square_size*10)) and phase == 'startup':
                for i in range(10):
                    y_start = square_size*i
                    y_end = y_start + square_size
                    if locate_y in range(y_start, y_end):
                        for j in range(10):
                            x_start = square_size*j
                            x_end = x_start+square_size
                            if locate_x in range(x_start, x_end):
                                # print(player_grid[y_start//square_size][x_start//square_size])
                                return (y_start//square_size, x_start//square_size, 'player')
            if locate_x in range((square_size*11), (1+square_size*21)) and phase == 'battle':
                for i in range(10):
                    y_start = square_size*i
                    y_end = y_start + square_size
                    if locate_y in range(y_start, y_end):
                        for j in range(10):
                            x_start = (square_size*11)+(square_size*j)
                            x_end = x_start+square_size
                            if locate_x in range(x_start, x_end):
                                # print(attack_grid[y_start//square_size][(x_start-(square_size*11))//square_size])
                                return (y_start//square_size, (x_start-(square_size*11))//square_size, 'attack')

    def update_square():
        while True:
            location = get_square()
            xcoord = location[1]
            ycoord = location[0]
            grid = location[2]
            # print(phase)
            # print(location)
            if phase == 'startup':
                check_here = player_grid[ycoord][xcoord]
                # print(check_here)
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

    def place_player_ships():
        while True:
            update_square()
            player_ship_count = 0
            for x in range(10):
                # print(player_grid[x])
                player_ship_count += player_grid[x].count('player')
                # print(player_ship_count)
            if player_ship_count == 15:
                break

    place_player_ships()
    # quit_game()

    def confirm_ship_placement():
        confirm_button, confirm_label = makebutton(
            (L-400)//2, H-200, L//2, H, "START GAME?", 'confirm_button', 'confirm_lable', 'green3', 'white', 15)
        confirm_button.draw(win)
        confirm_label.draw(win)
        reset_button, reset_label = makebutton(
            L-150, H-H, L, H-600, "RESET", 'reset_button', 'reset_lable', 'red', 'black', 20)
        reset_button.draw(win)
        reset_label.draw(win)
        while True:
            click = win.getMouse()
            clickX = click.getX()//1
            clickY = click.getY()//1
            if clickX in range((L-400)//2, L//2) and clickY in range(H-200, H):
                return None
            if clickX in range(L-150, L) and clickY in range(H-H, H-600):
                reset_player_grid()
                for s in player_squares:
                    s.undraw()
                print_player_grid()
                place_player_ships()

    confirm_ship_placement()
    phase = 'battle'

    def place_enemy_ships():
        enemy_ship_counter = 0
        # while enemy_ship_counter <15:
        #     occupied = False
        #     flip = random.randint(0,1)
        #     if attack_grid[i][j] != 'enemy':
        #         attack_grid[i][j] = 'enemy'
        #         enemy_ship_counter += 1
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

    place_enemy_ships()

    attack_here = -10

    def do_enemy_attack():
        most_row = player_grid[0]
        for x in range(10):
            ships_in_row = player_grid[x].count('player')
            if ships_in_row > most_row.count('player'):
                most_row = player_grid[x]
            # print(most_row)
        rand_row = random.randint(0, 9)
        rand_col = random.randint(0, 9)
        counter = 0
        # print(f"Step 1 {rand_row}, {rand_col}")
        if difficulty_level == 'easy':
            if player_grid[rand_row] == most_row:
                fail = random.randint(0, 1)
                # print(fail)
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
                print(f'start of loop {counter}')
                if counter%10 !=0:
                    print('went into the horizontal condition')
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
                    print('went into the vertical condition')
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
                # print(f"Changing rand_row to most_row, {rand_row}")
            if attack_here >= 0 and attack_here < 9:
                rand_col == attack_here + 1
                # print(f"attacking adjacent box {rand_col}")
            hard_fail = random.randint(1, 10)
            # print('fail?', hard_fail)
            if hard_fail > 7:
                if rand_row != 9:
                    rand_row += 1
                elif rand_row == 9:
                    rand_row -= 9
                # print(f"Moving rand_row off of most_row {rand_row}")
            # print(rand_row, rand_col)
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
        for x in range(10):
            # print(player_grid[x])
            player_ship_count += player_grid[x].count('player')
            enemy_ship_count += attack_grid[x].count('enemy')
        if player_ship_count == 0:
            return 2
        elif enemy_ship_count == 0:
            return 1
        else:
            return -1
        
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
        if difficulty_level == 'normal':
            bomb = random.randint(0,3)
            print(bomb)
            for location in bombs[bomb]:
                if player_grid[location[0]][location[1]] == 'player':
                    player_grid[location[0]][location[1]] = 'hit'
                elif player_grid[location[0]][location[1]] == 'empty':
                    player_grid[location[0]][location[1]] = 'miss'
            update_player_grid()
        if difficulty_level == 'hard':
            target = random.randint(0,9)
            for x in range(10):
                if player_grid[target][x] == 'player':
                    player_grid[target][x] = 'hit'
                elif player_grid[target][x] == 'empty':
                    player_grid[target][x] = 'miss'
            update_player_grid()
            
            
            
                        

                    
    def calculate_score(difficulty, turns, percent_ships):
        score = ((difficulty*percent_ships)//((turns-14)//2))*10000
        return score
                
        
            
            
    
    special_charger = 0 
    turn_count = 0
    while check_win() < 0:
        # print('started a new turn')
        update_square()
        update_attack_grid()
        turn_count += 1
        # print('player turn complete')
        attack_here = do_enemy_attack()
        # print('enemy turn complete')
        if attack_here == -10:
            special_charger += attack_here
        elif attack_here != -10:
            special_charger = 0
        if special_charger == -50:
            special_charger = 0 
            # print('called special attack')
            deploy_special_attack()
    if check_win() == 2:
        print('YOU LOSE')
        score = 0
    if check_win() == 1:
        print('YOU WIN')
        remaining_ships = 0
        for x in range(10):
            remaining_ships += player_grid[x].count('player')
        remaining_ships = (remaining_ships/15)*100
        if difficulty_level == 'easy':
            difficulty = 1
        elif difficulty_level == 'normal':
            difficulty = 2
        elif difficulty_level == 'hard':
            difficulty = 3
        score = calculate_score(difficulty, turn_count, remaining_ships)
    # quit_game()
    print(score)


if __name__ == "__main__":
    main()
