# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:42:11 2024

@author: lmbe0
"""

from graphics import *

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
    win = GraphWin("Battleship Homepage", L, H)
    win.setBackground("lightblue")
    graphical_objects = []  # Store all graphical objects for undrawing
    quit_button = init_top_menu(win, graphical_objects)
    init_diff_menu(win, graphical_objects, quit_button)
    return init_diff_menu(win, graphical_objects, quit_button)

def init_top_menu(win, graphical_objects):
    """Initializes the top menu elements."""
    # Add title
    title = Text(Point(L / 2, H / 8), "Welcome to Battleship!")
    title.setSize(20)
    title.setStyle("bold")
    title.draw(win)
    graphical_objects.append(title)

    # Add Quit button
    quit_button = Rectangle(Point(L - 100, 20), Point(L - 20, 60))
    quit_button.setFill("red")
    quit_button.draw(win)
    graphical_objects.append(quit_button)

    quit_text = Text(quit_button.getCenter(), "Quit")
    quit_text.setFill("white")
    quit_text.draw(win)
    graphical_objects.append(quit_text)

    # Return quit button for global click handling
    return quit_button

def init_diff_menu(win, graphical_objects, quit_button):
    """Initializes the difficulty selection menu."""
    # Add name input box
    name_label = Text(Point(L / 2.6, 150), "Enter Your Name:")
    name_label.setSize(12)
    name_label.draw(win)
    graphical_objects.append(name_label)

    name_box = Entry(Point(L / 2, 150), 20)
    name_box.draw(win)
    graphical_objects.append(name_box)

    # Add difficulty buttons
    difficulties = ["easy", "normal", "hard"]
    buttons = []
    for i, level in enumerate(difficulties):
        # Create button
        button = Rectangle(Point(L / 2.6, 200 + i * 50), Point(L - (L / 2.6), 240 + i * 50))
        button.setFill("white")
        button.draw(win)
        graphical_objects.append(button)

        # Add text to button
        button_text = Text(button.getCenter(), level)
        button_text.draw(win)
        graphical_objects.append(button_text)
        buttons.append((button, level))

    # Add submit button
    submit_button = Rectangle(Point(L / 2.3, 350 + 20), Point(L - (L / 2.3), 380 + 20))
    submit_button.setFill("white")
    submit_button.draw(win)
    graphical_objects.append(submit_button)

    submit_text = Text(submit_button.getCenter(), "Submit")
    submit_text.draw(win)
    graphical_objects.append(submit_text)

    selected_level = None
    while True:
        click = win.getMouse()

        # Check if the Quit button is clicked
        if is_clicked(click, quit_button):
            win.close()  # Ensure window closes
            return None  # Exit the loop and return

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
                return [win(user_name,selected_level)]

# Run the program
output = init_window()
if output is None:
    print("User exited the program.")
else:
    print(output)