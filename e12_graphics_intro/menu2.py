#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:47:42 2024

@author: mgh
"""

import graphics
from PIL import Image as PILImage


# Function to check if a point is inside a rectangle (button)
def is_clicked(point, rect):
    return (rect.getP1().getX() <= point.getX() <= rect.getP2().getX() and
            rect.getP1().getY() <= point.getY() <= rect.getP2().getY())

L = 1200
H = 800

def undraw_all(graphical_objects):
    """Undraws all graphical objects."""
    for obj in graphical_objects:
        obj.undraw()

def init_window():
    """Initializes the graphics window."""
    # Create window
    win = graphics.GraphWin("Battleship Homepage", L, H)
    win.setBackground("lightblue")
    graphical_objects = []  # Store all graphical objects for undrawing
    # init_top_menu(win, graphical_objects)
    # init_diff_menu(win, graphical_objects)
    return win, init_diff_menu(win, graphical_objects)



def init_top_menu(win, graphical_objects):
    """Initializes the top menu elements."""
    # Add title
    title = graphics.Text(graphics.Point(L / 2, H / 8), "Welcome to Battleship!")
    title.setSize(20)
    title.setStyle("bold")
    title.draw(win)
    graphical_objects.append(title)

def init_diff_menu(win, graphical_objects):
    # Add name input box
    name_label = graphics.Text(graphics.Point(L / 2.6, 150), "Enter Your Name:")
    name_label.setSize(12)
    name_label.draw(win)
    graphical_objects.append(name_label)

    name_box = graphics.Entry(graphics.Point(L / 2, 150), 20)
    name_box.draw(win)
    graphical_objects.append(name_box)

    # Add difficulty buttons
    difficulties = ["easy", "normal", "hard"]
    buttons = []
    for i, level in enumerate(difficulties):
        # Create button
        button = graphics.Rectangle(graphics.Point(L / 2.6, 200 + i * 50), graphics.Point(L - (L / 2.6), 240 + i * 50))
        button.setFill("white")
        button.draw(win)
        graphical_objects.append(button)

        # Add text to button
        button_text = graphics.Text(button.getCenter(), level)
        button_text.draw(win)
        graphical_objects.append(button_text)
        buttons.append((button, level))

    # Add submit button
    submit_button = graphics.Rectangle(graphics.Point(L / 2.3, 350 + 20), graphics.Point(L - (L / 2.3), 380 + 20))
    submit_button.setFill("white")
    submit_button.draw(win)
    graphical_objects.append(submit_button)

    submit_text = graphics.Text(submit_button.getCenter(), "Submit")
    submit_text.draw(win)
    graphical_objects.append(submit_text)

    selected_level = None
    while True:
        click = win.getMouse()

        # Check if difficulty button is clicked
        for button, level in buttons:
            if is_clicked(click, button):
                selected_level = level
                for b, _ in buttons:  # Highlight selected button
                    b.setFill("white")
                button.setFill("lightgreen")

        # Check if submit button is clicked
        if is_clicked(click, submit_button):
            user_name = name_box.getText().strip()  # Get and trim the entered name
            if selected_level and user_name:  # Ensure both inputs are valid
                undraw_all(graphical_objects)
                print(f"User Name: {user_name}")
                print(f"Selected Difficulty: {selected_level}")
                # win.close()
                return (user_name, selected_level)

# Run the program
# output = init_window()
# print(output)
window = ''
def win_screen(window):
    # win = graphics.GraphWin("My Window",L,H)
    # # Sets the coordinate system
    # win.setCoords(0,0, L, H)
    # # changes the background color
    # win.setBackground('black')
    """Display the 'YOU WIN' screen."""
    # Load and draw the win image
    # win_image = graphics.Image(graphics.Point(L/2, H/2), "win.png")
    # img_width = win_image.getWidth()
    # img_height = win_image.getHeight()
    # new_width = int(img_width / 2)
    # new_height = int(img_height / 2)
    # win_image.setWidth(new_width)
    # win_image.setHeight(new_height)
    # win_image.draw(win)
    # Load the lose image using PIL (Pillow)
    pil_image = PILImage.open("win.png")
    
    # Resize the image using Pillow
    new_width = L   # Resize to half the original size
    new_height = H
    pil_image = pil_image.resize((new_width, new_height))
    
    # Save the resized image temporarily (can use a different file name)
    pil_image.save("resized_win.png")
    
    # Load the resized image using the graphics library
    win_image = graphics.Image(graphics.Point(L / 2, H / 2), "resized_win.png")
    
    # Draw the image on the window
    win_image.draw(window)
    
    # Wait for a click to close the window
    window.getMouse()
    # window.close()
    win_image.undraw()


def lose_screen(window):
    """Display the 'YOU LOSE' screen."""
    # Create the window
    # win = graphics.GraphWin("My Window", L, H)
    # win.setCoords(0, 0, L, H)
    # win.setBackground('black')
    
    # Load the lose image using PIL (Pillow)
    pil_image = PILImage.open("lose.png")
    
    # Resize the image using Pillow
    new_width = L   # Resize to half the original size
    new_height = H
    pil_image = pil_image.resize((new_width, new_height))
    
    # Save the resized image temporarily (can use a different file name)
    pil_image.save("resized_lose.png")
    
    # Load the resized image using the graphics library
    lose_image = graphics.Image(graphics.Point(L / 2, H / 2), "resized_lose.png")
    
    # Draw the image on the window
    lose_image.draw(window)
    
    # Wait for a click to close the window
    window.getMouse()
    lose_image.undraw()

