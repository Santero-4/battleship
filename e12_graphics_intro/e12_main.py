#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:07:17 2024

@author: pfrank
"""

import graphics

def main():
    # creates the canvass window for the graphics
    win = graphics.GraphWin("My Window",300,200)

    # Sets the coordinate system
    win.setCoords(0,0, 300, 200)

    # changes the background color
    win.setBackground("pink") # <-- comment later

    # creates a red circle1 at a point pnt1, with a radius rad1
    pnt1 = graphics.Point(20,20)
    rad1 = 10
    circle1 = graphics.Circle(pnt1, rad1)
    color= "red"
    circle1.setFill(color)

    # indicates where to draw the circle
    circle1.draw(win)

    # creates a blue rec1 from lower-left pnt_a to upper-right pnt_b
    pnt_a = graphics.Point(25,25)
    pnt_b = graphics.Point(160,90)
    rec1 = graphics.Rectangle(pnt_a, pnt_b)
    rec1.setFill(graphics.color_rgb(64, 64, 255))

    # indicates where to draw the circle
    rec1.draw(win)

    # Todo: Add purple circle below this line


    # basic intereactive program
    click_point = win.getMouse()

    while True:
        click_point = win.getMouse()
        print(click_point)
        print(f"\tcircle.x: {pnt1.x}, circle.y: {pnt1.y}")
        print(f"\tclick.x: {click_point.x}, click.y: {click_point.y}")
        near_x = abs(click_point.x - pnt1.x) < rad1
        near_y = abs(click_point.y - pnt1.y) < rad1
        is_near = near_x and near_y
        if is_near:
            break

    print(f"You clicked the {color} point!")
    win.close()

if __name__ == "__main__":
    main()