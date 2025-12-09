#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:34:47 2024

@author: pfrank
"""

import graphics

WIDTH = 600
HEIGHT = 400

def main():
    # creates the canvass window for the graphics
    win = graphics.GraphWin("My Window",WIDTH,HEIGHT)
    
    # Sets the coordinate system
    win.setCoords(0,0, WIDTH, HEIGHT)
    
    # changes the background color
    win.setBackground(graphics.color_rgb(64, 64, 255)) # <-- comment later
    
    # load image
    yakImage = graphics.Image(graphics.Point(WIDTH/2,HEIGHT/2), "yak-small.png")
    yakImage.draw(win)
    
    # creates a red circle1 at a point pnt1, with a radius rad1
    pnt1 = graphics.Point(20,20)
    rad1 = 10
    circle1 = graphics.Circle(pnt1, rad1)
    color= "red"
    circle1.setFill(color)
    
    # indicates where to draw the circle
    circle1.draw(win)
    

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