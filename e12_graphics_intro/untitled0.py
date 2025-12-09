# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:23:59 2024

@author: lmbe0
"""

#Landing page 

graphics.import 

# Function to check if a point is inside a rectangle (button)
def is_clicked(point, rect):
    #is_clicked(point, rect) checks whether a point (e.g., a mouse click) is inside a given rectangle
    #point: A Point object (from graphics.py) representing the location of the click
    #rect: A Rectangle object (from graphics.py) representing the rectangular area to check
    return (rect.getP1().getX() <= point.getX() <= rect.getP2().getX() and
            rect.getP1().getY() <= point.getY() <= rect.getP2().getY())
    #rect.getP1(): Returns the first corner of the rectangle (bottom-left corner by default)
    #rect.getP2(): Returns the opposite corner of the rectangle (top-right corner by default)
    
def main():
    # Create window
    win = GraphWin("Battleship Homepage", 500, 400)
    win.setBackground("lightblue")

    # Add title
    title = Text(Point(250, 50), "Welcome to Battleship!")
    title.setSize(20)
    title.setStyle("bold")
    title.draw(win) #Draws the Text object onto the graphical window (win)

    # Add input box for name
    name_label = Text(Point(150, 150), "Enter Your Name:")
    name_label.setSize(12)
    name_label.draw(win)
    
    name_box = Entry(Point(300, 150), 20)
    name_box.draw(win)

    # Add difficulty buttons
    difficulties = ["Easy", "Medium", "Hard"]
    buttons = []
    #empty list buttons is created to store information about the buttons
    for i, level in enumerate(difficulties):
    #This loop iterates over the difficulties list.
        #i is the index of the current difficulty level (0, 1, 2 for "Easy", "Medium", "Hard").
            #used to calculate the vertical placement of the buttons, ensuring they don't overlap
        #level is the corresponding difficulty name ("Easy", "Medium", "Hard")
        
        # Create button
        button = Rectangle(Point(150, 200 + i * 50), Point(350, 240 + i * 50))
        button.setFill("white")
        button.draw(win)
        # Add text to button
        button_text = Text(button.getCenter(), level)
        #button.getCenter() calculates the center of the rectangle
        #Text(button.getCenter(), level) creates a Text object displaying the difficulty level (e.g., "Easy")
        button_text.draw(win)
        buttons.append((button, level))
        #Adds the rectangle object (button) and its associated difficulty level (level) as a tuple to the buttons list

    # Add submit button
    submit_button = Rectangle(Point(200, 350), Point(300, 380))
    submit_button.setFill("white")
    submit_button.draw(win)
    submit_text = Text(submit_button.getCenter(), "Submit")
    submit_text.draw(win)

    # Wait for user input
    selected_level = None #no difficulty has been selected yet
    user_name = None #no name yet
    while True:
        click = win.getMouse()
        #win.getMouse(): Waits for the user to click anywhere in the window and returns the position of the click as a Point object
        #while True loop keeps the program running until the user completes the required actions (selects a difficulty and enters their name)

        # Check if difficulty button is clicked
        for button, level in buttons:
            if is_clicked(click, button):
                selected_level = level
                for b, _ in buttons:  # Highlight selected button
                #each item in buttons is a tuple (button, level)
                #We only care about the button object here, so _ is used as a placeholder for the unused level
                    b.setFill("white")
                    #Ensures that any previously highlighted button (e.g., lightgreen) returns to its original state
                button.setFill("lightgreen")
                #Changes the color of this button to lightgreen to visually indicate that it has been selected

        # Check if submit button is clicked
        if is_clicked(click, submit_button):
            user_name = name_box.getText()
            if selected_level and user_name:  # Ensure both inputs are given
                break  # Exit loop when ready

    # Display results (for testing purposes)
    win.close()
    print(f"User Name: {user_name}")
    print(f"Selected Difficulty: {selected_level}")

# Run the program
main()